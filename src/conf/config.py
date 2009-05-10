#! /usr/bin/env python
# -*- coding: utf-8 -*-

# eLyXer configuration
# autogenerated from config file on 2009-05-10

class ContainerConfig(object):
  "Configuration class from config file"

  commands = {
      u'\\InsetSpace \\space{}':u'&nbsp;', u'\\InsetSpace \\thinspace{}':u' ', 
      u'\\InsetSpace ~':u'&nbsp;', u'\\SpecialChar \\@.':u'.', 
      u'\\SpecialChar \\ldots{}':u'…', 
      u'\\SpecialChar \\menuseparator':u'&nbsp;▷&nbsp;', 
      u'\\SpecialChar \\nobreakdash-':u'-', u'\\SpecialChar \\slash{}':u'/', 
      u'\\SpecialChar \\textcompwordmark{}':u'', u'\\backslash':u'\\', 
      }

  endings = {
      u'Abstract':u'\\end_layout', u'Align':u'\\end_layout', 
      u'Author':u'\\end_layout', u'BiblioCite':u'\\end_inset', 
      u'BiblioEntry':u'\\end_inset', u'Bibliography':u'\\end_layout', 
      u'BoxInset':u'\\end_inset', u'Branch':u'\\end_inset', 
      u'Caption':u'\\end_inset', u'Cell':u'</cell', 
      u'DeeperList':u'\\end_deeper', u'Description':u'\\end_layout', 
      u'ERT':u'\\end_inset', u'FlexCode':u'\\end_inset', 
      u'FlexURL':u'\\end_inset', u'Float':u'\\end_inset', 
      u'Footnote':u'\\end_inset', u'Formula':u'\\end_inset', 
      u'FormulaArray':u'\\end{array}', u'FormulaCases':u'\\end{cases}', 
      u'Image':u'\\end_inset', u'IndexEntry':u'\\end_inset', 
      u'InfoInset':u'\\end_inset', u'Inset':u'\\end_inset', 
      u'InsetText':u'\\end_inset', u'Label':u'\\end_inset', 
      u'Layout':u'\\end_layout', u'LayoutIndexEntry':u'\\end_inset', 
      u'List':u'\\end_layout', u'ListItem':u'\\end_layout', 
      u'ListOf':u'\\end_inset', u'Listing':u'\\end_inset', 
      u'LyxFooter':u'\\end_document', u'LyxHeader':u'\\end_header', 
      u'NewlineInset':u'\\end_inset', u'NomenclatureEntry':u'\\end_inset', 
      u'NomenclaturePrint':u'\\end_inset', u'Note':u'\\end_inset', 
      u'PrintIndex':u'\\end_inset', u'QuoteContainer':u'\\end_inset', 
      u'Reference':u'\\end_inset', u'Row':u'</row', 
      u'ShortTitle':u'\\end_inset', u'Space':u'\\end_inset', 
      u'Table':u'\\end_inset', u'TableOfContents':u'\\end_inset', 
      u'TableParser':u'</lyxtabular', u'Title':u'\\end_layout', 
      u'URL':u'\\end_inset', u'Wrap':u'\\end_inset', 
      }

  escapes = {
      u'&':u'&amp;', u'<':u'&lt;', u'>':u'&gt;', 
      }

  header = {
      u'branch':u'\\branch', u'endbranch':u'\\end_branch', 
      u'pdftitle':u'\\pdf_title', 
      }

  replaces = {
      u'\n':u'', u' -- ':u' — ', u'\'':u'’', u'`':u'‘', 
      }

  starts = {
      u'':u'StringContainer', u'#LyX':u'BlackBox', u'<cell':u'Cell', 
      u'<row':u'Row', u'\\align':u'Align', u'\\bar':u'BarredText', 
      u'\\bar default':u'BlackBox', u'\\bar no':u'BlackBox', 
      u'\\begin_body':u'BlackBox', u'\\begin_deeper':u'DeeperList', 
      u'\\begin_document':u'BlackBox', u'\\begin_header':u'LyxHeader', 
      u'\\begin_inset':u'Inset', u'\\begin_inset Box':u'BoxInset', 
      u'\\begin_inset Branch':u'Branch', u'\\begin_inset Caption':u'Caption', 
      u'\\begin_inset CommandInset bibitem':u'BiblioEntry', 
      u'\\begin_inset CommandInset citation':u'BiblioCite', 
      u'\\begin_inset CommandInset href':u'URL', 
      u'\\begin_inset CommandInset index_print':u'PrintIndex', 
      u'\\begin_inset CommandInset label':u'Label', 
      u'\\begin_inset CommandInset nomencl_print':u'NomenclaturePrint', 
      u'\\begin_inset CommandInset nomenclature':u'NomenclatureEntry', 
      u'\\begin_inset CommandInset ref':u'Reference', 
      u'\\begin_inset CommandInset toc':u'TableOfContents', 
      u'\\begin_inset ERT':u'ERT', 
      u'\\begin_inset Flex CharStyle:Code':u'FlexCode', 
      u'\\begin_inset Flex URL':u'FlexURL', u'\\begin_inset Float':u'Float', 
      u'\\begin_inset FloatList':u'ListOf', u'\\begin_inset Foot':u'Footnote', 
      u'\\begin_inset Formula':u'Formula', u'\\begin_inset Graphics':u'Image', 
      u'\\begin_inset Index':u'LayoutIndexEntry', 
      u'\\begin_inset Info':u'InfoInset', 
      u'\\begin_inset LatexCommand bibitem':u'BiblioEntry', 
      u'\\begin_inset LatexCommand cite':u'BiblioCite', 
      u'\\begin_inset LatexCommand htmlurl':u'URL', 
      u'\\begin_inset LatexCommand index':u'IndexEntry', 
      u'\\begin_inset LatexCommand label':u'Label', 
      u'\\begin_inset LatexCommand printindex':u'PrintIndex', 
      u'\\begin_inset LatexCommand ref':u'Reference', 
      u'\\begin_inset LatexCommand tableofcontents':u'TableOfContents', 
      u'\\begin_inset LatexCommand url':u'URL', 
      u'\\begin_inset Marginal':u'Footnote', 
      u'\\begin_inset Newline':u'NewlineInset', u'\\begin_inset Note':u'Note', 
      u'\\begin_inset OptArg':u'ShortTitle', 
      u'\\begin_inset Quotes':u'QuoteContainer', 
      u'\\begin_inset Tabular':u'Table', u'\\begin_inset Text':u'InsetText', 
      u'\\begin_inset Wrap':u'Wrap', u'\\begin_inset listings':u'Listing', 
      u'\\begin_inset space':u'Space', u'\\begin_layout':u'Layout', 
      u'\\begin_layout Abstract':u'Abstract', 
      u'\\begin_layout Author':u'Author', 
      u'\\begin_layout Bibliography':u'Bibliography', 
      u'\\begin_layout Description':u'Description', 
      u'\\begin_layout Enumerate':u'ListItem', 
      u'\\begin_layout Itemize':u'ListItem', u'\\begin_layout List':u'List', 
      u'\\begin_layout Title':u'Title', u'\\color':u'ColorText', 
      u'\\color inherit':u'BlackBox', u'\\color none':u'BlackBox', 
      u'\\emph default':u'BlackBox', u'\\emph off':u'BlackBox', 
      u'\\emph on':u'EmphaticText', u'\\end_body':u'LyxFooter', 
      u'\\family':u'TextFamily', u'\\family default':u'BlackBox', 
      u'\\family roman':u'BlackBox', u'\\hfill':u'Hfill', 
      u'\\labelwidthstring':u'BlackBox', u'\\lang':u'LangLine', 
      u'\\length':u'BlackBox', u'\\lyxformat':u'BlackBox', 
      u'\\lyxline':u'LyxLine', u'\\newline':u'Newline', 
      u'\\noindent':u'BlackBox', u'\\noun default':u'BlackBox', 
      u'\\noun off':u'BlackBox', u'\\noun on':u'VersalitasText', 
      u'\\paragraph_spacing':u'BlackBox', u'\\series bold':u'BoldText', 
      u'\\series default':u'BlackBox', u'\\series medium':u'BlackBox', 
      u'\\shape':u'ShapedText', u'\\shape default':u'BlackBox', 
      u'\\shape up':u'BlackBox', u'\\size':u'SizeText', 
      u'\\size normal':u'BlackBox', u'\\start_of_appendix':u'Appendix', 
      }

  string = {
      u'startcommand':u'\\', 
      }

class FormulaConfig(object):
  "Configuration class from config file"

  alphacommands = {
      u'\\Delta':u'Δ', u'\\Gamma':u'Γ', u'\\Upsilon':u'Υ', u'\\acute{A}':u'Á', 
      u'\\acute{E}':u'É', u'\\acute{I}':u'Í', u'\\acute{O}':u'Ó', 
      u'\\acute{U}':u'Ú', u'\\acute{a}':u'á', u'\\acute{e}':u'é', 
      u'\\acute{i}':u'í', u'\\acute{o}':u'ó', u'\\acute{u}':u'ú', 
      u'\\alpha':u'α', u'\\beta':u'β', u'\\delta':u'δ', u'\\epsilon':u'ε', 
      u'\\gamma':u'γ', u'\\lambda':u'λ', u'\\mu':u'μ', u'\\pi':u'π', 
      u'\\sigma':u'σ', u'\\tau':u'τ', u'\\tilde{N}':u'Ñ', u'\\tilde{n}':u'ñ', 
      u'\\varphi':u'φ', 
      }

  commands = {
      u'\\!':u'', u'\\%':u'%', u'\\,':u' ', u'\\:':u' ', 
      u'\\Longleftarrow':u'⟸', u'\\Longrightarrow':u'⟹', 
      u'\\Rightarrow':u' ⇒ ', u'\\\\':u'<br/>', u'\\_':u'_', 
      u'\\approx':u' ≈ ', u'\\backslash':u'\\', u'\\bigstar':u'★', 
      u'\\blacktriangleright':u'▶', u'\\bullet':u'•', u'\\cdot':u'⋅', 
      u'\\circ':u'○', u'\\cos':u'cos', u'\\cosh':u'cosh', u'\\dagger':u'†', 
      u'\\dashrightarrow':u' ⇢ ', u'\\ddagger':u'‡', u'\\ddots':u'⋱', 
      u'\\diamond':u'◇', u'\\displaystyle':u'', u'\\downarrow':u'↓', 
      u'\\end{array}':u'', u'\\exp':u'exp', u'\\ge':u' ≥ ', u'\\geq':u' ≥ ', 
      u'\\gets':u'←', u'\\implies':u'  ⇒  ', u'\\in':u' ∈ ', u'\\infty':u'∞', 
      u'\\int':u'<span class="bigsymbol">∫</span>', 
      u'\\intop':u'<span class="bigsymbol">∫</span>', 
      u'\\left(':u'<span class="bigsymbol">(</span>', 
      u'\\left[':u'<span class="bigsymbol">[</span>', u'\\leftarrow':u' ← ', 
      u'\\leq':u' ≤ ', u'\\lim':u'lim', u'\\ln':u'ln', u'\\log':u'log', 
      u'\\lyxlock':u'', u'\\ne':u' ≠ ', u'\\neq':u'≠', u'\\nonumber':u'', 
      u'\\not':u'¬', u'\\pm':u'±', u'\\prime':u'′', u'\\propto':u' ∝ ', 
      u'\\quad':u' ', u'\\right)':u'<span class="bigsymbol">)</span>', 
      u'\\right]':u'<span class="bigsymbol">]</span>', u'\\rightarrow':u' → ', 
      u'\\rightsquigarrow':u' ⇝ ', u'\\scriptscriptstyle':u'', 
      u'\\scriptstyle':u'', u'\\sim':u' ~ ', u'\\sin':u'sin', 
      u'\\sinh':u'sinh', u'\\sum':u'<span class="bigsymbol">∑</span>', 
      u'\\tanh':u'tanh', u'\\textstyle':u'', u'\\times':u' × ', u'\\to':u'→', 
      u'\\triangleright':u'▷', u'\\uparrow':u'↑', 
      }

  decoratingfunctions = {
      u'\\acute':u'´', u'\\breve':u'˘', u'\\check':u'ˇ', u'\\ddot':u'¨', 
      u'\\dot':u'˙', u'\\grave':u'`', u'\\hat':u'^', u'\\tilde':u'˜', 
      u'\\vec':u'→', 
      }

  endings = {
      u'Cell':u'&', u'Row':u'\\\\', u'common':u'\\end', u'complex':u'\\]', 
      u'endafter':u'}', u'endbefore':u'\\end{', 
      }

  fontfunctions = {
      u'\\boldsymbol':u'b', u'\\mathbb':u'span class="blackboard"', 
      u'\\mathbf':u'b', u'\\mathcal':u'span class="script"', 
      u'\\mathfrak':u'span class="fraktur"', u'\\mathit':u'i', 
      u'\\mathrm':u'span class="mathrm"', u'\\mathsf':u'span class="mathsf"', 
      u'\\mathtt':u'tt', u'\\text':u'span class="text"', 
      u'\\textipa':u'span class="textipa"', u'\\textrm':u'span class="mathrm"', 
      }

  fractionfunctions = [
      u'\\frac', u'\\nicefrac', 
      ]

  fractionspans = {
      u'first':u'span class="numerator"', 
      u'second':u'span class="denominator"', u'whole':u'span class="fraction"', 
      }

  limited = [
      u'\\sum', u'\\int', u'\\intop', 
      ]

  limits = [
      u'^', u'_', 
      ]

  modified = {
      u'\n':u'', u' ':u'', u'&':u'	', u'\'':u'’', u'+':u' + ', u',':u', ', 
      u'-':u' − ', u'/':u' ⁄ ', u'<':u' &lt; ', u'=':u' = ', u'>':u' &gt; ', 
      }

  onefunctions = {
      u'\\bar':u'span class="bar"', u'\\begin{array}':u'span class="arraydef"', 
      u'\\label':u'', u'\\mbox':u'span class="mbox"', 
      u'\\overline':u'span class="overline"', u'\\sqrt':u'span class="sqrt"', 
      u'\\underline':u'u', u'^':u'sup', u'_':u'sub', 
      }

  starts = {
      u'FormulaArray':u'\\begin{array}', u'FormulaCases':u'\\begin{cases}', 
      u'FormulaCommand':u'\\', u'beginafter':u'}', u'beginbefore':u'\\begin{', 
      u'complex':u'\\[', u'root':u'\\sqrt', u'simple':u'$', 
      }

  unmodified = [
      u'.', u'*', u'€', u'(', u')', u'[', u']', u':', u'·', u'!', u';', 
      ]

class GeneralConfig(object):
  "Configuration class from config file"

  version = {
      u'date':u'2009-05-10', u'number':u'0.21', 
      }

class SpaceConfig(object):
  "Configuration class from config file"

  spaces = {
      u'\\enskip{}':u' ', u'\\hfill{}':u' ', u'\\hspace*{\\fill}':u' ', 
      u'\\hspace*{}':u'', u'\\hspace{}':u' ', u'\\negthinspace{}':u'', 
      u'\\qquad{}':u'  ', u'\\quad{}':u' ', u'\\space{}':u'&nbsp;', 
      u'\\thinspace{}':u' ', u'~':u'&nbsp;', 
      }

class TranslationConfig(object):
  "Configuration class from config file"

  constants = {
      u'abstract':u'Abstract', 
      }

  floats = {
      u'algorithm':u'Listing ', u'figure':u'Figure ', u'table':u'Table ', 
      }

