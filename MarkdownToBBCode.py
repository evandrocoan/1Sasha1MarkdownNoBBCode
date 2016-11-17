#
#   Base on codes:
#   https://gist.github.com/sma/1513929
#   https://github.com/m3mnoch/MarkdownToBBCode/blob/master/MarkdownToBBCode.py
#


import sublime, sublime_plugin
import re, sys

class MarkdowntobbcodeCommand( sublime_plugin.TextCommand ):
    """
        You cannot parse the whole conversion from Markdown to BB Code only with regex.

        http://stackoverflow.com/a/1732454/4934640
        http://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags

        Changelog:

        2.0.0
        Fix issue `Disallow regular expression conversion between some tags`
        https://github.com/Kristinita/1Sasha1MarkdownNoBBCode/issues/1

        1.0.0
        Initial release by `Kristinita`.
    """

    codeBlock = []
    codeBlock.append( "```([^`]+)```"  ) # ```Multiline\n\code```
    codeBlock.append( "`([^`]+)`"      ) # `Code`
    codeBlock.append( "(?m)^\t(.*)$"   ) # Code fragment after tab
    codeBlock.append( "(?m)^ {4}(.*)$" ) # Code fragment after 4 spaces

    #
    # Notice: `alt` attribute not supported in many forums.
    #
    imageRegex      = "!\[(.*?)\]\((.*?)\)" # ![IMG description](URL of image)
    urlRegex        = "<(https?:\S+)>"      # <URL>
    urlAndLinkRegex = "\[(.*?)\]\((.*?)\)"  # [URL description](URL link)

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
                    Recursive function called by the `re.sub` for every non-overlapping occurrence of the pattern.

                    @param matchObject, an `sre.SRE_Match object` match object.
                """

                self.sourceCode = matchObject.group( targetGroup )
                # print( "( inline ) Receiving sourceCode as: `{0}`".format( self.sourceCode ) )

                #
                # Headers
                #
                self.sourceCode = re.sub( r"^#\s+(.*?)\s*$"   , "[h1]\\1[/h1]", self.sourceCode ) # Header first level
                self.sourceCode = re.sub( r"^##\s+(.*?)\s*$"  , "[h2]\\1[/h2]", self.sourceCode ) ## Header second level
                self.sourceCode = re.sub( r"^###\s+(.*?)\s*$" , "[h3]\\1[/h3]", self.sourceCode ) ### Header third level
                self.sourceCode = re.sub( r"^####\s+(.*?)\s*$", "[h4]\\1[/h4]", self.sourceCode ) #### Header fourth level

                # + Marked + List
                self.sourceCode = re.sub( r"(?m)^[-+*]\s+(.*)$", translate("№[list]\n[*]%s\n[/list]")  , self.sourceCode )

                # 1. Numbered 2. List
                self.sourceCode = re.sub( r"(?m)^\d+\.\s+(.*)$", translate("№[list=1]\n[*]%s\n[/list]"), self.sourceCode )

                # > Quote
                self.sourceCode = re.sub(r"^> (.*)$", "[quote]\\1[/quote]", self.sourceCode)

                # Thematic break
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
        # It re-uses several regexes, then it is needed to parse this before all the others,
        # because it needs several hacks (?<=\s), as `_` symbol often use in URLs.
        #
        self.singleTagContextParser( r"\*\*([^\*]+?)(?=\*\*)"              , "b", 2 ) # **Bold**
        self.singleTagContextParser( r"{0}([^{0}]+?)(?={0})".format( "\*" ), "i", 1 ) # *Italic*
        self.singleTagContextParser( r"__([^_]+?)(?=__)"                   , "b", 2 ) # __Bold__
        self.singleTagContextParser( r"{0}([^{0}]+?)(?={0})".format( "_"  ), "i", 1 ) # _Italic_
        self.singleTagContextParser( r"~~([\s\S]+?)(?=~~)"                 , "s", 2 ) # ~Strikethrough~

        #
        # Code
        #
        self.sourceCode = re.sub( r"{0}".format( self.codeBlock[ 0 ] ), "[code]\\1[/code]" , self.sourceCode )
        self.sourceCode = re.sub( r"{0}".format( self.codeBlock[ 1 ] ), "[code]\\1[/code]" , self.sourceCode )
        self.sourceCode = re.sub( r"{0}".format( self.codeBlock[ 2 ] ), "№[code]\\1[/code]", self.sourceCode )
        self.sourceCode = re.sub( r"{0}".format( self.codeBlock[ 3 ] ), "№[code]\\1[/code]", self.sourceCode )

        #
        # URL and images.
        #
        self.sourceCode = re.sub( r"{0}".format( self.imageRegex      ), "[img]\\2[/img]"    , self.sourceCode )
        self.sourceCode = re.sub( r"{0}".format( self.urlRegex        ), "[url]\\1[/url]"    , self.sourceCode )
        self.sourceCode = re.sub( r"{0}".format( self.urlAndLinkRegex ), "[url=\\2]\\1[/url]", self.sourceCode )

        #
        # Dependencies. Not delete these lines!
        # Clean the file using the flag symbol `№` indications.
        #

        # Enters on multiline mode `(?m)`, and asserts a line start `^` with `№` 0 or more times
        # not following it, until the end of the line `$`, i.e., passes a function pointer to
        # `inline`, and call it for every line which does not start with `№`.
        self.sourceCode = re.sub( r"(?m)^((?!№).*)$", translate(), self.sourceCode )

        self.sourceCode = re.sub( r"(?m)^№\["                , "[" , self.sourceCode )
        self.sourceCode = re.sub( r"\[/code]\n\[code(=.*?)?]", "\n", self.sourceCode )
        self.sourceCode = re.sub( r"\[/list]\n\[list(=1)?]\n", ""  , self.sourceCode )
        self.sourceCode = re.sub( r"\[/quote]\n\[quote]"     , "\n", self.sourceCode )

        return self.sourceCode

    def singleTagContextParser( self, regexExpression, bbCodeTag, replacementSize = 1 ):
        """
            Valid entrances are:
            _start without space between the _ and the first and last word.
            multilines are allowed. But one empty line get out the italic mode._

            But is does not have effect inside code blocks, neither URL's.
        """

        # self.sourceCode = re.sub( r"_([^_]+?)_"          , "[i]\\1[/i]", self.sourceCode )
        # for index in range( 0, len( self.sourceCode ) ):

        # Used to count how many iterations are necessary on the worst case scenario.
        matchesIterator = re.finditer( regexExpression, self.sourceCode )

        # The exclusion pattern to remove wrong blocks from being parsed.
        nextSearchPosition = 0
        exceptionRegex     = self.createRegexExceptoin()

        # Iterate until all the initial matches list to finish.
        for element in matchesIterator:

            # To perform a new search on the new updated string.
            match = re.search( regexExpression, self.sourceCode[ nextSearchPosition : ] )

            # Exit the parsing iteration when not more matches are found.
            if match is None:

                break

            print( "( singleTagContextParser ) Match: {0}".format( match.group( 0 ) ) )

            startIndex = match.start( 0 )
            endIndex   = match.end( 0 )

            startIndex = startIndex + nextSearchPosition
            endIndex   = endIndex   + nextSearchPosition

            nextSearchPosition = startIndex + replacementSize
            print( "nextSearchPosition: {0}".format( nextSearchPosition ) )

            if self.isWhereItMustNotToBe( startIndex, endIndex, exceptionRegex ):

                continue

            if endIndex + replacementSize > len( self.sourceCode ):

                self.sourceCode = self.sourceCode[ 0 : startIndex ] \
                                  + "[{0}]".format( bbCodeTag ) \
                                  + self.sourceCode[ startIndex + replacementSize : endIndex ] \
                                  + "[/{0}]".format( bbCodeTag )

            else:

                self.sourceCode = self.sourceCode[ 0 : startIndex ] \
                                  + "[{0}]".format( bbCodeTag ) \
                                  + self.sourceCode[ startIndex + replacementSize : endIndex ] \
                                  + "[/{0}]".format( bbCodeTag ) \
                                  + self.sourceCode[ endIndex + replacementSize : ]


    def createRegexExceptoin( self ):

        exceptionRegex  =  ""
        exceptionRegex +=  "(" + self.codeBlock[ 0 ]  + ")"
        exceptionRegex += "|(" + self.codeBlock[ 1 ]  + ")"
        exceptionRegex += "|(" + self.codeBlock[ 2 ]  + ")"
        exceptionRegex += "|(" + self.codeBlock[ 3 ]  + ")"
        exceptionRegex += "|(" + self.imageRegex      + ")"
        exceptionRegex += "|(" + self.urlRegex        + ")"
        exceptionRegex += "|(" + self.urlAndLinkRegex + ")"

        return exceptionRegex


    def isWhereItMustNotToBe( self, startIndex, endIndex, exceptionRegex ):
        """
            Valid entrances are:
            _start without space between the _ and the first and last word.
            multilines are allowed. But one empty line get out the italic mode._

            But is does not have effect inside code blocks, neither URL's.
        """

        matchesIterator = re.finditer( r"{0}".format( exceptionRegex ), self.sourceCode )

        for match in matchesIterator:

            print( "( isWhereItMustNotToBe ) Match: {0}".format( match.group( 0 ) ) )

            matchStart = match.start( 0 )
            matchEnd   = match.end( 0 )

            if ( ( matchStart <= startIndex ) and ( startIndex <= matchEnd ) ) \
               or ( ( matchStart <= endIndex ) and ( endIndex <= matchEnd ) ):

                print( "( isWhereItMustNotToBe ) Returning true." )
                return True

        return False




