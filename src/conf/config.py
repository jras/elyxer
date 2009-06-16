#! /usr/bin/env python
# -*- coding: utf-8 -*-

# eLyXer configuration
# autogenerated from config file on 2009-06-16

class ContainerConfig(object):
  "Configuration class from config file"

  endings = {
      u'Align':u'\\end_layout', u'BarredText':u'\\bar', 
      u'BoldText':u'\\series', u'Cell':u'</cell', u'ColorText':u'\\color', 
      u'EmphaticText':u'\\emph', u'Hfill':u'\\hfill', u'Inset':u'\\end_inset', 
      u'Layout':u'\\end_layout', u'LyxFooter':u'\\end_document', 
      u'LyxHeader':u'\\end_header', u'Row':u'</row', u'ShapedText':u'\\shape', 
      u'SizeText':u'\\size', u'TextFamily':u'\\family', 
      u'VersalitasText':u'\\noun', 
      }

  header = {
      u'branch':u'\\branch', u'endbranch':u'\\end_branch', 
      u'pdftitle':u'\\pdf_title', 
      }

  startendings = {
      u'\\begin_deeper':u'\\end_deeper', u'\\begin_inset':u'\\end_inset', 
      u'\\begin_layout':u'\\end_layout', 
      }

  starts = {
      u'':u'StringContainer', u'#LyX':u'BlackBox', u'</lyxtabular':u'BlackBox', 
      u'<cell':u'Cell', u'<column':u'Column', u'<row':u'Row', 
      u'\\align':u'Align', u'\\bar':u'BarredText', 
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
      u'\\begin_inset Index':u'IndexEntry', u'\\begin_inset Info':u'InfoInset', 
      u'\\begin_inset LatexCommand bibitem':u'BiblioEntry', 
      u'\\begin_inset LatexCommand cite':u'BiblioCite', 
      u'\\begin_inset LatexCommand htmlurl':u'URL', 
      u'\\begin_inset LatexCommand index':u'IndexEntry', 
      u'\\begin_inset LatexCommand label':u'Label', 
      u'\\begin_inset LatexCommand nomenclature':u'NomenclatureEntry', 
      u'\\begin_inset LatexCommand printindex':u'PrintIndex', 
      u'\\begin_inset LatexCommand printnomenclature':u'NomenclaturePrint', 
      u'\\begin_inset LatexCommand ref':u'Reference', 
      u'\\begin_inset LatexCommand tableofcontents':u'TableOfContents', 
      u'\\begin_inset LatexCommand url':u'URL', 
      u'\\begin_inset LatexCommand vref':u'Reference', 
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
      u'\\begin_layout Plain':u'PlainLayout', 
      u'\\begin_layout Standard':u'StandardLayout', 
      u'\\begin_layout Title':u'Title', u'\\color':u'ColorText', 
      u'\\color inherit':u'BlackBox', u'\\color none':u'BlackBox', 
      u'\\emph default':u'BlackBox', u'\\emph off':u'BlackBox', 
      u'\\emph on':u'EmphaticText', u'\\end_body':u'LyxFooter', 
      u'\\family':u'TextFamily', u'\\family default':u'BlackBox', 
      u'\\family roman':u'BlackBox', u'\\hfill':u'Hfill', 
      u'\\labelwidthstring':u'BlackBox', u'\\lang':u'LangLine', 
      u'\\length':u'BlackBox', u'\\lyxformat':u'LyXFormat', 
      u'\\lyxline':u'LyxLine', u'\\newline':u'Newline', 
      u'\\newpage':u'NewPage', u'\\noindent':u'BlackBox', 
      u'\\noun default':u'BlackBox', u'\\noun off':u'BlackBox', 
      u'\\noun on':u'VersalitasText', u'\\paragraph_spacing':u'BlackBox', 
      u'\\series bold':u'BoldText', u'\\series default':u'BlackBox', 
      u'\\series medium':u'BlackBox', u'\\shape':u'ShapedText', 
      u'\\shape default':u'BlackBox', u'\\shape up':u'BlackBox', 
      u'\\size':u'SizeText', u'\\size normal':u'BlackBox', 
      u'\\start_of_appendix':u'Appendix', 
      }

  string = {
      u'startcommand':u'\\', 
      }

  table = {
      u'headers':[u'<lyxtabular',u'<features',], 
      }

class EscapeConfig(object):
  "Configuration class from config file"

  chars = {
      u'\n':u'', u' -- ':u' — ', u'\'':u'’', u'`':u'‘', 
      }

  commands = {
      u'\\InsetSpace \\space{}':u'&nbsp;', u'\\InsetSpace \\thinspace{}':u' ', 
      u'\\InsetSpace ~':u'&nbsp;', u'\\SpecialChar \\-':u'', 
      u'\\SpecialChar \\@.':u'.', u'\\SpecialChar \\ldots{}':u'…', 
      u'\\SpecialChar \\menuseparator':u'&nbsp;▷&nbsp;', 
      u'\\SpecialChar \\nobreakdash-':u'-', u'\\SpecialChar \\slash{}':u'/', 
      u'\\SpecialChar \\textcompwordmark{}':u'', u'\\backslash':u'\\', 
      }

  entities = {
      u'&':u'&amp;', u'<':u'&lt;', u'>':u'&gt;', 
      }

  html = {
      u'/>':u'>', 
      }

  nonunicode = {
      u' ':u' ', 
      }

class FootnoteConfig(object):
  "Configuration class from config file"

  constants = {
      u'postfrom':u'] ', u'postto':u'→] ', u'prefrom':u'[→', u'preto':u' [', 
      }

class FormulaConfig(object):
  "Configuration class from config file"

  alphacommands = {
      u'\\Delta':u'Δ', u'\\Gamma':u'Γ', u'\\Upsilon':u'Υ', u'\\acute{A}':u'Á', 
      u'\\acute{E}':u'É', u'\\acute{I}':u'Í', u'\\acute{O}':u'Ó', 
      u'\\acute{U}':u'Ú', u'\\acute{a}':u'á', u'\\acute{e}':u'é', 
      u'\\acute{i}':u'í', u'\\acute{o}':u'ó', u'\\acute{u}':u'ú', 
      u'\\alpha':u'α', u'\\beta':u'β', u'\\delta':u'δ', u'\\epsilon':u'ε', 
      u'\\gamma':u'γ', u'\\lambda':u'λ', u'\\mu':u'μ', u'\\nu':u'ν', 
      u'\\pi':u'π', u'\\sigma':u'σ', u'\\tau':u'τ', u'\\tilde{N}':u'Ñ', 
      u'\\tilde{n}':u'ñ', u'\\varphi':u'φ', 
      }

  array = {
      u'begin':u'\\begin', u'cellseparator':u'&', u'end':u'\\end', 
      u'rowseparator':u'\\\\', 
      }

  commands = {
      u'\\!':u'', u'\\%':u'%', u'\\,':u' ', u'\\:':u' ', u'\\Delta':u'Δ', 
      u'\\Downarrow':u'⇓', u'\\Gamma':u'Γ', u'\\Im':u'ℑ', u'\\Lambda':u'Λ', 
      u'\\Leftarrow':u'⇐', u'\\Leftrightarrow':u' ⇔ ', u'\\Longleftarrow':u'⟸', 
      u'\\Longrightarrow':u'⟹', u'\\Omega':u'Ω', u'\\Phi':u'Φ', u'\\Pi':u'Π', 
      u'\\Pr':u'Pr', u'\\Psi':u'Ψ', u'\\Re':u'ℜ', u'\\Rightarrow':u' ⇒ ', 
      u'\\Sigma':u'Σ', u'\\Theta':u'Θ', u'\\Uparrow':u'⇑', 
      u'\\Updownarrow':u'⇕', u'\\Upsilon':u'Υ', u'\\Xi':u'Ξ', u'\\\\':u'<br/>', 
      u'\\_':u'_', u'\\aleph':u'ℵ', u'\\alpha':u'α', u'\\amalg':u'∐', 
      u'\\angle':u'∠', u'\\approx':u' ≈ ', u'\\arccos':u'arccos', 
      u'\\arcsin':u'arcsin', u'\\arctan':u'arctan', u'\\arg':u'arg', 
      u'\\ast':u'∗', u'\\asymp':u'≍', u'\\backslash':u'\\', u'\\beta':u'β', 
      u'\\bigcap':u'∩', u'\\bigcirc':u'○', u'\\bigcup':u'∪', u'\\bigodot':u'⊙', 
      u'\\bigoplus':u'⊕', u'\\bigotimes':u'⊗', u'\\bigsqcup':u'⊔', 
      u'\\bigstar':u'★', u'\\biguplus':u'⊎', u'\\bigvee':u'∨', 
      u'\\bigwedge':u'∧', u'\\blacktriangleright':u'▶', u'\\bot':u'⊥', 
      u'\\bowtie':u'⋈', u'\\box':u'▫', u'\\bullet':u'•', u'\\cap':u'∩', 
      u'\\cdot':u'⋅', u'\\cdots':u'⋯', u'\\chi':u'χ', u'\\circ':u'○', 
      u'\\clubsuit':u'♣', u'\\cong':u'≅', u'\\coprod':u'∐', u'\\cos':u'cos', 
      u'\\cosh':u'cosh', u'\\cot':u'cot', u'\\coth':u'coth', u'\\csc':u'csc', 
      u'\\cup':u'∪', u'\\dagger':u'†', u'\\dashrightarrow':u' ⇢ ', 
      u'\\dashv':u'⊣', u'\\ddagger':u'‡', u'\\ddots':u'⋱', u'\\deg':u'deg', 
      u'\\delta':u'δ', u'\\det':u'det', u'\\diamond':u'◇', 
      u'\\diamondsuit':u'♦', u'\\dim':u'dim', u'\\displaystyle':u'', 
      u'\\div':u'÷', u'\\doteq':u'≐', u'\\downarrow':u'↓', u'\\ell':u'ℓ', 
      u'\\emptyset':u'∅', u'\\end{array}':u'', u'\\epsilon':u'ε', 
      u'\\equiv':u' ≡ ', u'\\eta':u'η', u'\\exists':u'∃', u'\\exp':u'exp', 
      u'\\forall':u'∀', u'\\gamma':u'γ', u'\\gcd':u'gcd', u'\\ge':u' ≥ ', 
      u'\\geq':u' ≥ ', u'\\gets':u'←', u'\\gg':u'≫', u'\\hbar':u'ℏ', 
      u'\\heartsuit':u'♥', u'\\hom':u'hom', u'\\hookleftarrow':u'↩', 
      u'\\hookrightarrow':u'↪', u'\\implies':u'  ⇒  ', u'\\in':u' ∈ ', 
      u'\\inf':u'inf', u'\\infty':u'∞', 
      u'\\int':u'<span class="bigsymbol">∫</span>', 
      u'\\intop':u'<span class="bigsymbol">∫</span>', u'\\iota':u'ι', 
      u'\\kappa':u'κ', u'\\ker':u'ker', u'\\lambda':u'λ', u'\\langle':u'⟨', 
      u'\\le':u'≤', u'\\leadsto':u'⇝', u'\\leftarrow':u' ← ', 
      u'\\leftharpoondown':u'↽', u'\\leftharpoonup':u'↼', 
      u'\\leftrightarrow':u'↔', u'\\leq':u' ≤ ', u'\\lg':u'lg', 
      u'\\lim':u'lim', u'\\liminf':u'liminf', u'\\limsup':u'limsup', 
      u'\\ll':u'≪', u'\\ln':u'ln', u'\\log':u'log', u'\\longleftarrow':u'⟵', 
      u'\\longrightarrow':u'⟶', u'\\lyxlock':u'', u'\\mapsto':u'↦', 
      u'\\max':u'max', u'\\mho':u'℧', u'\\mid':u'∣', u'\\min':u'min', 
      u'\\models':u'⊨', u'\\mp':u'∓', u'\\mu':u'μ', u'\\nabla':u'∇', 
      u'\\ne':u' ≠ ', u'\\nearrow':u'↗', u'\\neg':u'¬', u'\\neq':u' ≠ ', 
      u'\\ni':u'∋', u'\\nonumber':u'', u'\\not':u'¬', u'\\not\\in':u' ∉ ', 
      u'\\nu':u'ν', u'\\nwarrow':u'↖', u'\\odot':u'⊙', u'\\oint':u'∮', 
      u'\\omega':u'ω', u'\\ominus':u'⊖', u'\\oplus':u'⊕', u'\\oslash':u'⊘', 
      u'\\otimes':u'⊗', u'\\parallel':u'∥', u'\\partial':u'∂', u'\\perp':u'⊥', 
      u'\\phi':u'φ', u'\\pi':u'π', u'\\pm':u'±', u'\\prec':u'≺', 
      u'\\preceq':u'≼', u'\\prime':u'′', 
      u'\\prod':u'<span class="bigsymbol">∏</span>', u'\\prompto':u'∝', 
      u'\\propto':u' ∝ ', u'\\psi':u'ψ', u'\\quad':u' ', u'\\rangle':u'⟩', 
      u'\\rho':u'ρ', u'\\rightarrow':u' → ', u'\\rightharpooondown':u'⇁', 
      u'\\rightharpooonup':u'⇀', u'\\rightleftharpoons':u'⇌', 
      u'\\rightsquigarrow':u' ⇝ ', u'\\scriptscriptstyle':u'', 
      u'\\scriptstyle':u'', u'\\searrow':u'↘', u'\\sec':u'sec', 
      u'\\setminus':u'∖', u'\\sigma':u'σ', u'\\sim':u' ~ ', u'\\simeq':u'≃', 
      u'\\sin':u'sin', u'\\sinh':u'sinh', u'\\spadesuit':u'♠', u'\\sqcap':u'⊓', 
      u'\\sqcup':u'⊔', u'\\sqsubset':u'⊏', u'\\sqsubseteq':u'⊑', 
      u'\\sqsupset':u'⊐', u'\\sqsupseteq':u'⊒', u'\\square':u'□', 
      u'\\star':u'⋆', u'\\subset':u' ⊂ ', u'\\subseteq':u'⊆', u'\\succ':u'≻', 
      u'\\succeq':u'≽', u'\\sum':u'<span class="bigsymbol">∑</span>', 
      u'\\sup':u'sup', u'\\supset':u' ⊃ ', u'\\supseteq':u'⊇', u'\\surd':u'√', 
      u'\\swarrow':u'↙', u'\\tan':u'tan', u'\\tanh':u'tanh', u'\\tau':u'τ', 
      u'\\textstyle':u'', u'\\theta':u'θ', u'\\times':u' × ', u'\\to':u'→', 
      u'\\top':u'⊤', u'\\triangleleft':u'⊲', u'\\triangleright':u'▷', 
      u'\\unlhd':u'⊴', u'\\unrhl':u'⊵', u'\\uparrow':u'↑', 
      u'\\updownarrow':u'↕', u'\\uplus':u'⊎', u'\\upsilon':u'υ', 
      u'\\varphi':u'φ', u'\\varpi':u'ϖ', u'\\varrho':u'ϱ', u'\\varsigma':u'ς', 
      u'\\vartheta':u'ϑ', u'\\vdash':u'⊢', u'\\vee':u'∨', u'\\wedge':u'∧', 
      u'\\wp':u'℘', u'\\wr':u'≀', u'\\xi':u'ξ', u'\\zeta':u'ζ', u'\\{':u'{', 
      u'\\}':u'}', 
      }

  decoratingfunctions = {
      u'\\acute':u'´', u'\\breve':u'˘', u'\\check':u'ˇ', u'\\ddot':u'¨', 
      u'\\dot':u'˙', u'\\grave':u'`', u'\\hat':u'^', u'\\overleftarrow':u'⟵', 
      u'\\overrightarrow':u'⟶', u'\\tilde':u'˜', u'\\vec':u'→', 
      }

  endings = {
      u'bracket':u'}', u'complex':u'\\]', u'endafter':u'}', 
      u'endbefore':u'\\end{', u'squarebracket':u']', 
      }

  fontfunctions = {
      u'\\boldsymbol':u'b', u'\\mathbb':u'span class="blackboard"', 
      u'\\mathbf':u'b', u'\\mathcal':u'span class="script"', 
      u'\\mathfrak':u'span class="fraktur"', u'\\mathit':u'i', 
      u'\\mathrm':u'span class="mathrm"', u'\\mathsf':u'span class="mathsf"', 
      u'\\mathtt':u'tt', u'\\textrm':u'span class="mathrm"', 
      }

  fractionfunctions = {
      
      u'\\frac':[u'span class="fraction"',u'span class="numerator"',u'',u'span class="denominator"',], 
      u'\\nicefrac':[u'span class="fraction"',u'sup class="numerator"',u'⁄',u'sub class="denominator"',], 
      }

  hybridfunctions = {
      u'\\sqrt':[u'sqrt',u'span class="sqrt"',u'sup',], 
      u'\\unit':[u'font',u'span class="unit"',u'',], 
      }

  labelfunctions = {
      u'\\label':u'a class="eqnumber" name="#"', 
      }

  limits = {
      u'commands':[u'\\sum',u'\\int',u'\\intop',], u'operands':[u'^',u'_',], 
      }

  literalfunctions = {
      u'\\mbox':u'span class="mbox"', u'\\text':u'span class="text"', 
      u'\\textipa':u'span class="textipa"', 
      }

  modified = {
      u'\n':u'', u' ':u'', u'&':u'	', u'\'':u'’', u'+':u' + ', u',':u', ', 
      u'-':u' − ', u'/':u' ⁄ ', u'<':u' &lt; ', u'=':u' = ', u'>':u' &gt; ', 
      }

  onefunctions = {
      u'\\bar':u'span class="bar"', u'\\begin{array}':u'span class="arraydef"', 
      u'\\bigl':u'span class="bigsymbol"', u'\\bigr':u'span class="bigsymbol"', 
      u'\\hphantom':u'span class="phantom"', u'\\left':u'span class="symbol"', 
      u'\\overline':u'span class="overline"', 
      u'\\phantom':u'span class="phantom"', u'\\right':u'span class="symbol"', 
      u'\\underline':u'u', u'\\vphantom':u'span class="phantom"', 
      }

  starts = {
      u'beginafter':u'}', u'beginbefore':u'\\begin{', u'bracket':u'{', 
      u'command':u'\\', u'complex':u'\\[', u'simple':u'$', 
      u'squarebracket':u'[', 
      }

  symbolfunctions = {
      u'^':u'sup', u'_':u'sub', 
      }

  unmodified = {
      
      u'characters':[u'.',u'*',u'€',u'(',u')',u'[',u']',u':',u'·',u'!',u';',u'|',], 
      }

class GeneralConfig(object):
  "Configuration class from config file"

  version = {
      u'date':u'2009-06-16', u'number':u'0.27', 
      }

class NumberingConfig(object):
  "Configuration class from config file"

  layouts = {
      
      u'ordered':[u'Chapter',u'Section',u'Subsection',u'Subsubsection',u'Paragraph',], 
      u'unique':[u'Part',u'Book',], 
      }

class StyleConfig(object):
  "Configuration class from config file"

  quotes = {
      u'ald':u'»', u'als':u'›', u'ard':u'«', u'ars':u'‹', u'eld':u'“', 
      u'els':u'‘', u'erd':u'”', u'ers':u'’', u'fld':u'«', u'fls':u'‹', 
      u'frd':u'»', u'frs':u'›', u'gld':u'„', u'gls':u'‚', u'grd':u'“', 
      u'grs':u'‘', u'pld':u'„', u'pls':u'‚', u'prd':u'”', u'prs':u'’', 
      u'sld':u'”', u'srd':u'”', 
      }

  spaces = {
      u'\\enskip{}':u' ', u'\\hfill{}':u' ', u'\\hspace*{\\fill}':u' ', 
      u'\\hspace*{}':u'', u'\\hspace{}':u' ', u'\\negthinspace{}':u'', 
      u'\\qquad{}':u'  ', u'\\quad{}':u' ', u'\\space{}':u'&nbsp;', 
      u'\\thinspace{}':u' ', u'~':u'&nbsp;', 
      }

class TagConfig(object):
  "Configuration class from config file"

  barred = {
      u'under':u'u', 
      }

  boxes = {
      u'Framed':u'div class="framed"', u'Frameless':u'div class="frameless"', 
      }

  family = {
      u'sans':u'span class="sans"', u'typewriter':u'tt', 
      }

  layouts = {
      u'Center':u'div', u'Chapter':u'h1', u'Date':u'h2', u'LyX-Code':u'pre', 
      u'Paragraph':u'div', u'Part':u'h1', u'Quotation':u'blockquote', 
      u'Quote':u'blockquote', u'Section':u'h2', u'Subsection':u'h3', 
      u'Subsubsection':u'h4', 
      }

  listitems = {
      u'Enumerate':u'ol', u'Itemize':u'ul', 
      }

  notes = {
      u'Comment':u'', u'Greyedout':u'span class="greyedout"', u'Note':u'', 
      }

  shaped = {
      u'italic':u'i', u'slanted':u'i', u'smallcaps':u'span class="versalitas"', 
      }

class TranslationConfig(object):
  "Configuration class from config file"

  constants = {
      u'abstract':u'Abstract', u'bibliography':u'Bibliography', 
      u'index':u'Index', u'nomenclature':u'Nomenclature', 
      u'toc':u'Table of Contents', 
      }

  floats = {
      u'algorithm':u'Listing ', u'figure':u'Figure ', u'listing':u'Listing ', 
      u'table':u'Table ', 
      }

  lists = {
      u'algorithm':u'List of Listings', u'figure':u'List of Figures', 
      u'table':u'List of Tables', 
      }

