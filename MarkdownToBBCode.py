#
# 	Base on codes:
# 	https://gist.github.com/sma/1513929
#	https://github.com/m3mnoch/MarkdownToBBCode/blob/master/MarkdownToBBCode.py
#


import sublime, sublime_plugin
import re, sys

class MarkdowntobbcodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		allcontent = sublime.Region(0, self.view.size())

		regionString = self.markdown_to_bbcode(str(self.view.substr(allcontent)))
		self.view.replace(edit, allcontent, regionString)

	def markdown_to_bbcode(self,sourceCode):

		def translate(p="%s", g=1):

			def inline(m):
				sourceCode = m.group(g)
				#
				# Headers
				#
				sourceCode = re.sub(r"^#\s+(.*?)\s*$", "[h1]\\1[/h1]", sourceCode)   # # Header first level
				sourceCode = re.sub(r"^##\s+(.*?)\s*$", "[h2]\\1[/h2]", sourceCode)  # ## Header second level
				sourceCode = re.sub(r"^###\s+(.*?)\s*$", "[h3]\\1[/h3]", sourceCode) # ### Header third level
				sourceCode = re.sub(r"^####\s+(.*?)\s*$", "[h4]\\1[/h4]", sourceCode)# #### Header fourth level
				#
				# Lists
				#
				sourceCode = re.sub(r"(?m)^[-+*]\s+(.*)$", translate("№[list]\n[*]%s\n[/list]"), sourceCode) # + Marked + List
				sourceCode = re.sub(r"(?m)^\d+\.\s+(.*)$", translate("№[list=1]\n[*]%s\n[/list]"), sourceCode) # 1. Numbered 2. List
				#
				# Quote
				#
				sourceCode = re.sub(r"^> (.*)$", "[quote]\\1[/quote]", sourceCode) # > Quote
				#
				# Thematic break
				#
				sourceCode = re.sub(r"^-{3}(\s*)$", "[hr]", sourceCode)
				return p % sourceCode
			return inline

		#
		# URL and images
		#
		sourceCode = re.sub(r"!\[(.*?)\]\((.*?)\)", "[img]\\2[/img]", sourceCode)   # ![IMG description](URL of image), alt attribute not supported in many forums
		sourceCode = re.sub(r"\[(.*?)\]\((.*?)\)", "[url=\\2]\\1[/url]", sourceCode)# [URL description](URL link)
		sourceCode = re.sub(r"<(https?:\S+)>", "[url]\\1[/url]", sourceCode)        # <URL>
		#
		# Code, create a function for this and an Automated Unit Test
		#
		sourceCode = re.sub(r"```([^`]+)```" , "[code]\\1[/code]" , sourceCode) # ```Multiline\n\code```
		sourceCode = re.sub(r"`([^`]+)`"     , "[code]\\1[/code]" , sourceCode) # `Code`
		sourceCode = re.sub(r"(?m)^ {4}(.*)$", "№[code]\\1[/code]", sourceCode) # Code fragment after 4 spaces
		sourceCode = re.sub(r"(?m)^\t(.*)$"  , "№[code]\\1[/code]", sourceCode) # Code fragment after tab
		#
		# Bold and italic
		#
		sourceCode = re.sub(r"_{2}([\s\S]+?)_{2}", "[b]\\1[/b]", sourceCode)  # __Bold__
		sourceCode = re.sub(r"_([^_]+?)_", "[i]\\1[/i]", sourceCode)   		# _Italic_ Needs hack (?<=\s), because _ symbol often use in URLs
		sourceCode = re.sub(r"\*{2}([\s\S]+?)\*{2}", "[b]\\1[/b]", sourceCode)# **Bold**
		sourceCode = re.sub(r"\*([^\*]+?)\*", "[i]\\1[/i]", sourceCode)       # *Italic*.
		#
		# Strikethrough text
		#
		sourceCode = re.sub(r"~{2}([\s\S]+?)~{2}", "[sourceCode]\\1[\sourceCode]", sourceCode)
		#
		# Dependencies. Not delete these lines!
		#
		sourceCode = re.sub(r"(?m)^((?!№).*)$", translate(), sourceCode)
		sourceCode = re.sub(r"(?m)^№\[", "[", sourceCode)
		sourceCode = re.sub(r"\[/code]\n\[code(=.*?)?]", "\n", sourceCode)
		sourceCode = re.sub(r"\[/list]\n\[list(=1)?]\n", "", sourceCode)
		sourceCode = re.sub(r"\[/quote]\n\[quote]", "\n", sourceCode)

		return sourceCode
