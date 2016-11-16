#
#   Base on codes:
#   https://gist.github.com/sma/1513929
#   https://github.com/m3mnoch/MarkdownToBBCode/blob/master/MarkdownToBBCode.py
#


import sublime, sublime_plugin
import re, sys

class MarkdowntobbcodeCommand( sublime_plugin.TextCommand ):
    """
        You cannot parse the ~whole conversion from Markdown to BB Code only with regex.

        http://stackoverflow.com/a/1732454/4934640
        http://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags
    """

    def run( self, edit ):

        allcontent      = sublime.Region( 0, self.view.size() )
        self.sourceCode = str( self.view.substr( allcontent ) )

        self.view.replace( edit, allcontent, self.markdown_to_bbcode() )

    def markdown_to_bbcode( self ):

        def translate( formattingRule = "%s", targetGroup = 1 ):
            """
                # Here is a closure in python:
                def makeInc(x):
                  def inc(y):
                     # x is "closed" in the definition of inc
                     return y + x

                return inc

                inc5 = makeInc(5)
                inc10 = makeInc(10)

                inc5 (5) # returns 10
                inc10(5) # returns 15

                @param formattingRule, is a string format for the `%` parsing.
                @param targetGroup   , is the group to retrieve from the `matchObject`.

                @return a function pointer.
            """

            # print( "( translate ) targetGroup: {0}, sourceCode: {1}".format( targetGroup, self.sourceCode ) )

            def inline( matchObject ):
                """
                    Recursive function called by the `re.sub` for every non-overlapping occurrence of pattern.

                    @param matchObject, an `sre.SRE_Match object` match object.
                """

                self.sourceCode = matchObject.group( targetGroup )
                # print( "( inline ) Receiving sourceCode as: `{0}`".format( self.sourceCode ) )

                #
                # Headers
                #
                self.sourceCode = re.sub( r"^#\s+(.*?)\s*$"   , "[h1]\\1[/h1]", self.sourceCode ) # # Header first level
                self.sourceCode = re.sub( r"^##\s+(.*?)\s*$"  , "[h2]\\1[/h2]", self.sourceCode ) # ## Header second level
                self.sourceCode = re.sub( r"^###\s+(.*?)\s*$" , "[h3]\\1[/h3]", self.sourceCode ) # ### Header third level
                self.sourceCode = re.sub( r"^####\s+(.*?)\s*$", "[h4]\\1[/h4]", self.sourceCode ) # #### Header fourth level

                #
                # Lists
                #
                self.sourceCode = re.sub( r"(?m)^[-+*]\s+(.*)$", translate("№[list]\n[*]%s\n[/list]")  , self.sourceCode ) # + Marked + List
                self.sourceCode = re.sub( r"(?m)^\d+\.\s+(.*)$", translate("№[list=1]\n[*]%s\n[/list]"), self.sourceCode ) # 1. Numbered 2. List

                #
                # Quote
                #
                self.sourceCode = re.sub(r"^> (.*)$", "[quote]\\1[/quote]", self.sourceCode) # > Quote

                #
                # Thematic break
                #
                self.sourceCode = re.sub(r"^-{3}(\s*)$", "[hr]", self.sourceCode)

                # Format the `sourceCode` into to `formattingRule` with the `%` formatting rule.
                # print( "( inline ) Leaving   sourceCode as: `{0}`".format( formattingRule % self.sourceCode ) )
                return formattingRule % self.sourceCode

            #
            # The `inline` function is effectively an anonymous function here, since the variable scope in which
            # it was created is no longer accessible to the caller.
            #
            # See:
            # http://ynniv.com/blog/2007/08/closures-in-python.html
            # http://stackoverflow.com/questions/6629876/how-to-make-an-anonymous-function-in-python-without-christening-it
            #
            return inline

        #
        # Bold and italic, need to parse this before all the others, as it re-uses its regex's.
        #
        self.sourceCode = re.sub( r"_{2}([\s\S]+?)_{2}"  , "[b]\\1[/b]", self.sourceCode ) # __Bold__

        # _Italic_ Needs hack (?<=\s), because _ symbol often use in URLs
        self.italicParsing( "_" )
        self.italicParsing( "\*" )

        self.sourceCode = re.sub( r"\*{2}([\s\S]+?)\*{2}", "[b]\\1[/b]", self.sourceCode ) # **Bold**

        #
        # Code, create a function for this and an Automated Unit Test
        #
        self.sourceCode = re.sub( r"```([^`]+)```" , "[code]\\1[/code]" , self.sourceCode ) # ```Multiline\n\code```
        self.sourceCode = re.sub( r"`([^`]+)`"     , "[code]\\1[/code]" , self.sourceCode ) # `Code`
        self.sourceCode = re.sub( r"(?m)^ {4}(.*)$", "№[code]\\1[/code]", self.sourceCode ) # Code fragment after 4 spaces
        self.sourceCode = re.sub( r"(?m)^\t(.*)$"  , "№[code]\\1[/code]", self.sourceCode ) # Code fragment after tab

        #
        # URL and images.
        #
        # ![IMG description](URL of image), alt attribute not supported in many forums
        self.sourceCode = re.sub( r"!\[(.*?)\]\((.*?)\)", "[img]\\2[/img]"    , self.sourceCode )
        self.sourceCode = re.sub( r"\[(.*?)\]\((.*?)\)" , "[url=\\2]\\1[/url]", self.sourceCode ) # [URL description](URL link)
        self.sourceCode = re.sub( r"<(https?:\S+)>"     , "[url]\\1[/url]"    , self.sourceCode ) # <URL>

        #
        # Strikethrough text
        #
        self.sourceCode = re.sub( r"~{2}([\s\S]+?)~{2}", "[s]\\1[\s]", self.sourceCode )

        #
        # Dependencies. Not delete these lines!
        #

        # Enters on multiline mode `(?m)`, and asserts a line start `^` with `№` 0 or more times
        # not following it, until the end of the line `$`.
        self.sourceCode = re.sub( r"(?m)^((?!№).*)$"          , translate(), self.sourceCode )

        self.sourceCode = re.sub( r"(?m)^№\["                 , "["        , self.sourceCode )
        self.sourceCode = re.sub( r"\[/code]\n\[code(=.*?)?]" , "\n"       , self.sourceCode )
        self.sourceCode = re.sub( r"\[/list]\n\[list(=1)?]\n" , ""         , self.sourceCode )
        self.sourceCode = re.sub( r"\[/quote]\n\[quote]"      , "\n"       , self.sourceCode )

        return self.sourceCode

    def italicParsing( self, specialChar ):
        """
            Valid entrances are:
            _start without space between the _ and the first and last word.
            multilines are allowed. But one empty line get out the italic mode._

            But is does not have effect inside code blocks, neither URL's.
        """
        # self.sourceCode = re.sub( r"_([^_]+?)_"          , "[i]\\1[/i]", self.sourceCode )
        # for index in range( 0, len( self.sourceCode ) ):

        matchesIterator = re.finditer( r"{0}([^{0}]+?)(?={0})".format( specialChar ), self.sourceCode )

        for match in matchesIterator:

            print( "( italicParsing ) Match: {0}".format( match.group( 0 ) ) )

            startIndex = match.start( 0 )
            endIndex   = match.end( 0 )

            if self.isWhereItMustNotToBe( startIndex, endIndex ):

                continue

            if endIndex + 1 > len( self.sourceCode ):

                self.sourceCode = self.sourceCode[ 0 : startIndex ] \
                                  + "[i]" \
                                  + self.sourceCode[ startIndex+1 : endIndex ] \
                                  + "[/i]"

            else:

                self.sourceCode = self.sourceCode[ 0 : startIndex ] \
                                  + "[i]" \
                                  + self.sourceCode[ startIndex + 1 : endIndex ] \
                                  + "[/i]" \
                                  + self.sourceCode[ endIndex + 1 : ]

    def isWhereItMustNotToBe( self, startIndex, endIndex ):
        """
            Valid entrances are:
            _start without space between the _ and the first and last word.
            multilines are allowed. But one empty line get out the italic mode._

            But is does not have effect inside code blocks, neither URL's.
        """

        # matchesIterator = re.finditer( r"(\[url=?.*\].*\[\\url\])|(\[img\].*\[\\img\])", self.sourceCode )
        matchesIterator = re.finditer( r"(!\[(.*?)\]\((.*?)\))|(\[(.*?)\]\((.*?)\))|(<(https?:\S+)>)|(```([^`]+)```)", self.sourceCode )

        for match in matchesIterator:

            print( "( isWhereItMustNotToBe ) Match: {0}".format( match.group( 0 ) ) )

            matchStart = match.start( 0 )
            matchEnd   = match.end( 0 )

            if ( ( matchStart <= startIndex ) and ( startIndex <= matchEnd ) ) \
               or ( ( matchStart <= endIndex ) and ( endIndex <= matchEnd ) ):

                print( "( isWhereItMustNotToBe ) Returning true." )
                return True

        return False




