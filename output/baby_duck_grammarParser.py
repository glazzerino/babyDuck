# Generated from .\baby_duck_grammar.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,38,263,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,1,0,1,0,5,0,65,8,0,10,0,
        12,0,68,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,76,8,1,1,1,1,1,1,2,5,2,81,
        8,2,10,2,12,2,84,9,2,1,2,1,2,1,2,1,2,1,3,1,3,5,3,92,8,3,10,3,12,
        3,95,9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,3,4,104,8,4,1,5,1,5,1,6,1,6,
        1,6,1,6,1,6,1,7,1,7,1,7,1,7,3,7,117,8,7,1,8,1,8,1,9,1,9,1,10,1,10,
        1,10,3,10,126,8,10,1,10,1,10,1,10,1,11,1,11,3,11,133,8,11,1,11,1,
        11,1,11,3,11,138,8,11,5,11,140,8,11,10,11,12,11,143,9,11,1,12,1,
        12,1,12,5,12,148,8,12,10,12,12,12,151,9,12,3,12,153,8,12,1,13,1,
        13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,3,14,165,8,14,1,14,1,
        14,1,14,1,14,1,15,1,15,1,15,1,16,1,16,4,16,176,8,16,11,16,12,16,
        177,1,17,1,17,1,17,5,17,183,8,17,10,17,12,17,186,9,17,1,17,1,17,
        1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,20,
        1,20,1,20,1,20,1,20,1,20,3,20,208,8,20,1,20,1,20,1,21,1,21,1,21,
        1,22,1,22,1,23,1,23,1,23,1,23,3,23,221,8,23,1,24,1,24,1,24,1,24,
        3,24,227,8,24,1,25,1,25,1,26,1,26,3,26,233,8,26,1,26,1,26,3,26,237,
        8,26,3,26,239,8,26,1,27,1,27,1,28,1,28,1,28,1,28,1,29,1,29,1,29,
        3,29,250,8,29,1,29,1,29,1,29,1,30,1,30,1,30,5,30,258,8,30,10,30,
        12,30,261,9,30,1,30,1,66,0,31,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,0,5,1,0,8,
        11,1,0,13,18,2,0,36,36,38,38,1,0,31,32,1,0,33,34,257,0,62,1,0,0,
        0,2,71,1,0,0,0,4,82,1,0,0,0,6,89,1,0,0,0,8,103,1,0,0,0,10,105,1,
        0,0,0,12,107,1,0,0,0,14,112,1,0,0,0,16,118,1,0,0,0,18,120,1,0,0,
        0,20,122,1,0,0,0,22,132,1,0,0,0,24,152,1,0,0,0,26,154,1,0,0,0,28,
        158,1,0,0,0,30,170,1,0,0,0,32,173,1,0,0,0,34,179,1,0,0,0,36,191,
        1,0,0,0,38,199,1,0,0,0,40,201,1,0,0,0,42,211,1,0,0,0,44,214,1,0,
        0,0,46,216,1,0,0,0,48,222,1,0,0,0,50,228,1,0,0,0,52,238,1,0,0,0,
        54,240,1,0,0,0,56,242,1,0,0,0,58,246,1,0,0,0,60,254,1,0,0,0,62,66,
        5,1,0,0,63,65,9,0,0,0,64,63,1,0,0,0,65,68,1,0,0,0,66,67,1,0,0,0,
        66,64,1,0,0,0,67,69,1,0,0,0,68,66,1,0,0,0,69,70,5,1,0,0,70,1,1,0,
        0,0,71,72,5,2,0,0,72,73,5,35,0,0,73,75,5,3,0,0,74,76,3,32,16,0,75,
        74,1,0,0,0,75,76,1,0,0,0,76,77,1,0,0,0,77,78,3,4,2,0,78,3,1,0,0,
        0,79,81,3,28,14,0,80,79,1,0,0,0,81,84,1,0,0,0,82,80,1,0,0,0,82,83,
        1,0,0,0,83,85,1,0,0,0,84,82,1,0,0,0,85,86,5,4,0,0,86,87,3,6,3,0,
        87,88,5,5,0,0,88,5,1,0,0,0,89,93,5,6,0,0,90,92,3,8,4,0,91,90,1,0,
        0,0,92,95,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,96,1,0,0,0,95,93,
        1,0,0,0,96,97,5,7,0,0,97,7,1,0,0,0,98,104,3,12,6,0,99,104,3,40,20,
        0,100,104,3,36,18,0,101,104,3,58,29,0,102,104,3,20,10,0,103,98,1,
        0,0,0,103,99,1,0,0,0,103,100,1,0,0,0,103,101,1,0,0,0,103,102,1,0,
        0,0,104,9,1,0,0,0,105,106,7,0,0,0,106,11,1,0,0,0,107,108,5,35,0,
        0,108,109,5,12,0,0,109,110,3,14,7,0,110,111,5,3,0,0,111,13,1,0,0,
        0,112,116,3,46,23,0,113,114,3,16,8,0,114,115,3,14,7,0,115,117,1,
        0,0,0,116,113,1,0,0,0,116,117,1,0,0,0,117,15,1,0,0,0,118,119,7,1,
        0,0,119,17,1,0,0,0,120,121,7,2,0,0,121,19,1,0,0,0,122,123,5,19,0,
        0,123,125,5,20,0,0,124,126,3,22,11,0,125,124,1,0,0,0,125,126,1,0,
        0,0,126,127,1,0,0,0,127,128,5,21,0,0,128,129,5,3,0,0,129,21,1,0,
        0,0,130,133,3,14,7,0,131,133,3,0,0,0,132,130,1,0,0,0,132,131,1,0,
        0,0,133,141,1,0,0,0,134,137,5,22,0,0,135,138,3,14,7,0,136,138,3,
        0,0,0,137,135,1,0,0,0,137,136,1,0,0,0,138,140,1,0,0,0,139,134,1,
        0,0,0,140,143,1,0,0,0,141,139,1,0,0,0,141,142,1,0,0,0,142,23,1,0,
        0,0,143,141,1,0,0,0,144,149,3,26,13,0,145,146,5,22,0,0,146,148,3,
        26,13,0,147,145,1,0,0,0,148,151,1,0,0,0,149,147,1,0,0,0,149,150,
        1,0,0,0,150,153,1,0,0,0,151,149,1,0,0,0,152,144,1,0,0,0,152,153,
        1,0,0,0,153,25,1,0,0,0,154,155,5,35,0,0,155,156,5,23,0,0,156,157,
        3,10,5,0,157,27,1,0,0,0,158,159,3,30,15,0,159,160,5,20,0,0,160,161,
        3,24,12,0,161,162,5,21,0,0,162,164,5,24,0,0,163,165,3,32,16,0,164,
        163,1,0,0,0,164,165,1,0,0,0,165,166,1,0,0,0,166,167,3,6,3,0,167,
        168,5,25,0,0,168,169,5,3,0,0,169,29,1,0,0,0,170,171,3,10,5,0,171,
        172,5,35,0,0,172,31,1,0,0,0,173,175,5,26,0,0,174,176,3,34,17,0,175,
        174,1,0,0,0,176,177,1,0,0,0,177,175,1,0,0,0,177,178,1,0,0,0,178,
        33,1,0,0,0,179,184,5,35,0,0,180,181,5,22,0,0,181,183,5,35,0,0,182,
        180,1,0,0,0,183,186,1,0,0,0,184,182,1,0,0,0,184,185,1,0,0,0,185,
        187,1,0,0,0,186,184,1,0,0,0,187,188,5,23,0,0,188,189,3,10,5,0,189,
        190,5,3,0,0,190,35,1,0,0,0,191,192,5,27,0,0,192,193,3,6,3,0,193,
        194,5,28,0,0,194,195,5,20,0,0,195,196,3,14,7,0,196,197,5,21,0,0,
        197,198,5,3,0,0,198,37,1,0,0,0,199,200,5,28,0,0,200,39,1,0,0,0,201,
        202,5,29,0,0,202,203,5,20,0,0,203,204,3,14,7,0,204,205,5,21,0,0,
        205,207,3,6,3,0,206,208,3,42,21,0,207,206,1,0,0,0,207,208,1,0,0,
        0,208,209,1,0,0,0,209,210,5,3,0,0,210,41,1,0,0,0,211,212,5,30,0,
        0,212,213,3,6,3,0,213,43,1,0,0,0,214,215,7,3,0,0,215,45,1,0,0,0,
        216,220,3,48,24,0,217,218,3,44,22,0,218,219,3,46,23,0,219,221,1,
        0,0,0,220,217,1,0,0,0,220,221,1,0,0,0,221,47,1,0,0,0,222,226,3,52,
        26,0,223,224,3,50,25,0,224,225,3,48,24,0,225,227,1,0,0,0,226,223,
        1,0,0,0,226,227,1,0,0,0,227,49,1,0,0,0,228,229,7,4,0,0,229,51,1,
        0,0,0,230,239,3,56,28,0,231,233,3,54,27,0,232,231,1,0,0,0,232,233,
        1,0,0,0,233,236,1,0,0,0,234,237,5,35,0,0,235,237,3,18,9,0,236,234,
        1,0,0,0,236,235,1,0,0,0,237,239,1,0,0,0,238,230,1,0,0,0,238,232,
        1,0,0,0,239,53,1,0,0,0,240,241,7,3,0,0,241,55,1,0,0,0,242,243,5,
        20,0,0,243,244,3,14,7,0,244,245,5,21,0,0,245,57,1,0,0,0,246,247,
        5,35,0,0,247,249,5,20,0,0,248,250,3,60,30,0,249,248,1,0,0,0,249,
        250,1,0,0,0,250,251,1,0,0,0,251,252,5,21,0,0,252,253,5,3,0,0,253,
        59,1,0,0,0,254,259,3,14,7,0,255,256,5,22,0,0,256,258,3,14,7,0,257,
        255,1,0,0,0,258,261,1,0,0,0,259,257,1,0,0,0,259,260,1,0,0,0,260,
        61,1,0,0,0,261,259,1,0,0,0,23,66,75,82,93,103,116,125,132,137,141,
        149,152,164,177,184,207,220,226,232,236,238,249,259
    ]

class baby_duck_grammarParser ( Parser ):

    grammarFileName = "baby_duck_grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\"'", "'program'", "';'", "'main'", 
                     "'end'", "'{'", "'}'", "'int'", "'float'", "'bool'", 
                     "'void'", "'='", "'<'", "'>'", "'!='", "'=='", "'<='", 
                     "'>=c'", "'print'", "'('", "')'", "','", "':'", "'['", 
                     "']'", "'var'", "'do'", "'while'", "'if'", "'else'", 
                     "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "INT", 
                      "WS", "FLOAT" ]

    RULE_string = 0
    RULE_program = 1
    RULE_program_post_var = 2
    RULE_body = 3
    RULE_statement = 4
    RULE_type = 5
    RULE_assign = 6
    RULE_expression = 7
    RULE_rel_op = 8
    RULE_cte = 9
    RULE_print = 10
    RULE_print_helper = 11
    RULE_f_param_list = 12
    RULE_f_param_list_helper = 13
    RULE_funcs = 14
    RULE_function_id = 15
    RULE_vars = 16
    RULE_vars_declarations = 17
    RULE_cycle = 18
    RULE_while_keyword = 19
    RULE_condition = 20
    RULE_condition_else = 21
    RULE_operator = 22
    RULE_exp = 23
    RULE_term = 24
    RULE_term_operator = 25
    RULE_factor = 26
    RULE_factor_operator = 27
    RULE_parenthesized_expression = 28
    RULE_f_call = 29
    RULE_f_call_helper = 30

    ruleNames =  [ "string", "program", "program_post_var", "body", "statement", 
                   "type", "assign", "expression", "rel_op", "cte", "print", 
                   "print_helper", "f_param_list", "f_param_list_helper", 
                   "funcs", "function_id", "vars", "vars_declarations", 
                   "cycle", "while_keyword", "condition", "condition_else", 
                   "operator", "exp", "term", "term_operator", "factor", 
                   "factor_operator", "parenthesized_expression", "f_call", 
                   "f_call_helper" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    ID=35
    INT=36
    WS=37
    FLOAT=38

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)




    def string(self):

        localctx = baby_duck_grammarParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(baby_duck_grammarParser.T__0)
            self.state = 66
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 63
                    self.matchWildcard() 
                self.state = 68
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 69
            self.match(baby_duck_grammarParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(baby_duck_grammarParser.ID, 0)

        def program_post_var(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.Program_post_varContext,0)


        def vars_(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.VarsContext,0)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = baby_duck_grammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(baby_duck_grammarParser.T__1)
            self.state = 72
            self.match(baby_duck_grammarParser.ID)
            self.state = 73
            self.match(baby_duck_grammarParser.T__2)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 74
                self.vars_()


            self.state = 77
            self.program_post_var()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Program_post_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.BodyContext,0)


        def funcs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(baby_duck_grammarParser.FuncsContext)
            else:
                return self.getTypedRuleContext(baby_duck_grammarParser.FuncsContext,i)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_program_post_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram_post_var" ):
                listener.enterProgram_post_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram_post_var" ):
                listener.exitProgram_post_var(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram_post_var" ):
                return visitor.visitProgram_post_var(self)
            else:
                return visitor.visitChildren(self)




    def program_post_var(self):

        localctx = baby_duck_grammarParser.Program_post_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_program_post_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3840) != 0):
                self.state = 79
                self.funcs()
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 85
            self.match(baby_duck_grammarParser.T__3)
            self.state = 86
            self.body()
            self.state = 87
            self.match(baby_duck_grammarParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(baby_duck_grammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(baby_duck_grammarParser.StatementContext,i)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = baby_duck_grammarParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(baby_duck_grammarParser.T__5)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 35031351296) != 0):
                self.state = 90
                self.statement()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 96
            self.match(baby_duck_grammarParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.AssignContext,0)


        def condition(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.ConditionContext,0)


        def cycle(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.CycleContext,0)


        def f_call(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.F_callContext,0)


        def print_(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.PrintContext,0)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = baby_duck_grammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statement)
        try:
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.assign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self.condition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 100
                self.cycle()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 101
                self.f_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 102
                self.print_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = baby_duck_grammarParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3840) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(baby_duck_grammarParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = baby_duck_grammarParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(baby_duck_grammarParser.ID)
            self.state = 108
            self.match(baby_duck_grammarParser.T__11)
            self.state = 109
            self.expression()
            self.state = 110
            self.match(baby_duck_grammarParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.ExpContext,0)


        def rel_op(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.Rel_opContext,0)


        def expression(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = baby_duck_grammarParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.exp()
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 516096) != 0):
                self.state = 113
                self.rel_op()
                self.state = 114
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rel_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_rel_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRel_op" ):
                listener.enterRel_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRel_op" ):
                listener.exitRel_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRel_op" ):
                return visitor.visitRel_op(self)
            else:
                return visitor.visitChildren(self)




    def rel_op(self):

        localctx = baby_duck_grammarParser.Rel_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_rel_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 516096) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(baby_duck_grammarParser.INT, 0)

        def FLOAT(self):
            return self.getToken(baby_duck_grammarParser.FLOAT, 0)

        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_cte

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCte" ):
                listener.enterCte(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCte" ):
                listener.exitCte(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCte" ):
                return visitor.visitCte(self)
            else:
                return visitor.visitChildren(self)




    def cte(self):

        localctx = baby_duck_grammarParser.CteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_cte)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            _la = self._input.LA(1)
            if not(_la==36 or _la==38):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def print_helper(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.Print_helperContext,0)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_print

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)




    def print_(self):

        localctx = baby_duck_grammarParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_print)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(baby_duck_grammarParser.T__18)
            self.state = 123
            self.match(baby_duck_grammarParser.T__19)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 384400621570) != 0):
                self.state = 124
                self.print_helper()


            self.state = 127
            self.match(baby_duck_grammarParser.T__20)
            self.state = 128
            self.match(baby_duck_grammarParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_helperContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(baby_duck_grammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(baby_duck_grammarParser.ExpressionContext,i)


        def string(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(baby_duck_grammarParser.StringContext)
            else:
                return self.getTypedRuleContext(baby_duck_grammarParser.StringContext,i)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_print_helper

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_helper" ):
                listener.enterPrint_helper(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_helper" ):
                listener.exitPrint_helper(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint_helper" ):
                return visitor.visitPrint_helper(self)
            else:
                return visitor.visitChildren(self)




    def print_helper(self):

        localctx = baby_duck_grammarParser.Print_helperContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_print_helper)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 31, 32, 35, 36, 38]:
                self.state = 130
                self.expression()
                pass
            elif token in [1]:
                self.state = 131
                self.string()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 134
                self.match(baby_duck_grammarParser.T__21)
                self.state = 137
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [20, 31, 32, 35, 36, 38]:
                    self.state = 135
                    self.expression()
                    pass
                elif token in [1]:
                    self.state = 136
                    self.string()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class F_param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def f_param_list_helper(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(baby_duck_grammarParser.F_param_list_helperContext)
            else:
                return self.getTypedRuleContext(baby_duck_grammarParser.F_param_list_helperContext,i)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_f_param_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterF_param_list" ):
                listener.enterF_param_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitF_param_list" ):
                listener.exitF_param_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitF_param_list" ):
                return visitor.visitF_param_list(self)
            else:
                return visitor.visitChildren(self)




    def f_param_list(self):

        localctx = baby_duck_grammarParser.F_param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_f_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 144
                self.f_param_list_helper()
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==22:
                    self.state = 145
                    self.match(baby_duck_grammarParser.T__21)
                    self.state = 146
                    self.f_param_list_helper()
                    self.state = 151
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class F_param_list_helperContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(baby_duck_grammarParser.ID, 0)

        def type_(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.TypeContext,0)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_f_param_list_helper

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterF_param_list_helper" ):
                listener.enterF_param_list_helper(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitF_param_list_helper" ):
                listener.exitF_param_list_helper(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitF_param_list_helper" ):
                return visitor.visitF_param_list_helper(self)
            else:
                return visitor.visitChildren(self)




    def f_param_list_helper(self):

        localctx = baby_duck_grammarParser.F_param_list_helperContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_f_param_list_helper)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(baby_duck_grammarParser.ID)
            self.state = 155
            self.match(baby_duck_grammarParser.T__22)
            self.state = 156
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_id(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.Function_idContext,0)


        def f_param_list(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.F_param_listContext,0)


        def body(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.BodyContext,0)


        def vars_(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.VarsContext,0)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_funcs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncs" ):
                listener.enterFuncs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncs" ):
                listener.exitFuncs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncs" ):
                return visitor.visitFuncs(self)
            else:
                return visitor.visitChildren(self)




    def funcs(self):

        localctx = baby_duck_grammarParser.FuncsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_funcs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.function_id()
            self.state = 159
            self.match(baby_duck_grammarParser.T__19)
            self.state = 160
            self.f_param_list()
            self.state = 161
            self.match(baby_duck_grammarParser.T__20)
            self.state = 162
            self.match(baby_duck_grammarParser.T__23)
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 163
                self.vars_()


            self.state = 166
            self.body()
            self.state = 167
            self.match(baby_duck_grammarParser.T__24)
            self.state = 168
            self.match(baby_duck_grammarParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_idContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.TypeContext,0)


        def ID(self):
            return self.getToken(baby_duck_grammarParser.ID, 0)

        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_function_id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_id" ):
                listener.enterFunction_id(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_id" ):
                listener.exitFunction_id(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_id" ):
                return visitor.visitFunction_id(self)
            else:
                return visitor.visitChildren(self)




    def function_id(self):

        localctx = baby_duck_grammarParser.Function_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_function_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.type_()
            self.state = 171
            self.match(baby_duck_grammarParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vars_declarations(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(baby_duck_grammarParser.Vars_declarationsContext)
            else:
                return self.getTypedRuleContext(baby_duck_grammarParser.Vars_declarationsContext,i)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_vars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVars" ):
                listener.enterVars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVars" ):
                listener.exitVars(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVars" ):
                return visitor.visitVars(self)
            else:
                return visitor.visitChildren(self)




    def vars_(self):

        localctx = baby_duck_grammarParser.VarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_vars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(baby_duck_grammarParser.T__25)
            self.state = 175 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 174
                self.vars_declarations()
                self.state = 177 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==35):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vars_declarationsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(baby_duck_grammarParser.ID)
            else:
                return self.getToken(baby_duck_grammarParser.ID, i)

        def type_(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.TypeContext,0)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_vars_declarations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVars_declarations" ):
                listener.enterVars_declarations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVars_declarations" ):
                listener.exitVars_declarations(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVars_declarations" ):
                return visitor.visitVars_declarations(self)
            else:
                return visitor.visitChildren(self)




    def vars_declarations(self):

        localctx = baby_duck_grammarParser.Vars_declarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_vars_declarations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(baby_duck_grammarParser.ID)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 180
                self.match(baby_duck_grammarParser.T__21)
                self.state = 181
                self.match(baby_duck_grammarParser.ID)
                self.state = 186
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 187
            self.match(baby_duck_grammarParser.T__22)
            self.state = 188
            self.type_()
            self.state = 189
            self.match(baby_duck_grammarParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CycleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.BodyContext,0)


        def expression(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_cycle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCycle" ):
                listener.enterCycle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCycle" ):
                listener.exitCycle(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCycle" ):
                return visitor.visitCycle(self)
            else:
                return visitor.visitChildren(self)




    def cycle(self):

        localctx = baby_duck_grammarParser.CycleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_cycle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(baby_duck_grammarParser.T__26)
            self.state = 192
            self.body()
            self.state = 193
            self.match(baby_duck_grammarParser.T__27)
            self.state = 194
            self.match(baby_duck_grammarParser.T__19)
            self.state = 195
            self.expression()
            self.state = 196
            self.match(baby_duck_grammarParser.T__20)
            self.state = 197
            self.match(baby_duck_grammarParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_keywordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_while_keyword

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_keyword" ):
                listener.enterWhile_keyword(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_keyword" ):
                listener.exitWhile_keyword(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_keyword" ):
                return visitor.visitWhile_keyword(self)
            else:
                return visitor.visitChildren(self)




    def while_keyword(self):

        localctx = baby_duck_grammarParser.While_keywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_while_keyword)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(baby_duck_grammarParser.T__27)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.ExpressionContext,0)


        def body(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.BodyContext,0)


        def condition_else(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.Condition_elseContext,0)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = baby_duck_grammarParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(baby_duck_grammarParser.T__28)
            self.state = 202
            self.match(baby_duck_grammarParser.T__19)
            self.state = 203
            self.expression()
            self.state = 204
            self.match(baby_duck_grammarParser.T__20)
            self.state = 205
            self.body()
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 206
                self.condition_else()


            self.state = 209
            self.match(baby_duck_grammarParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condition_elseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.BodyContext,0)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_condition_else

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition_else" ):
                listener.enterCondition_else(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition_else" ):
                listener.exitCondition_else(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition_else" ):
                return visitor.visitCondition_else(self)
            else:
                return visitor.visitChildren(self)




    def condition_else(self):

        localctx = baby_duck_grammarParser.Condition_elseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_condition_else)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(baby_duck_grammarParser.T__29)
            self.state = 212
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperator" ):
                return visitor.visitOperator(self)
            else:
                return visitor.visitChildren(self)




    def operator(self):

        localctx = baby_duck_grammarParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            _la = self._input.LA(1)
            if not(_la==31 or _la==32):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.TermContext,0)


        def operator(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.OperatorContext,0)


        def exp(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.ExpContext,0)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = baby_duck_grammarParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.term()
            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31 or _la==32:
                self.state = 217
                self.operator()
                self.state = 218
                self.exp()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.FactorContext,0)


        def term_operator(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.Term_operatorContext,0)


        def term(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.TermContext,0)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = baby_duck_grammarParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.factor()
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33 or _la==34:
                self.state = 223
                self.term_operator()
                self.state = 224
                self.term()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Term_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_term_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm_operator" ):
                listener.enterTerm_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm_operator" ):
                listener.exitTerm_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm_operator" ):
                return visitor.visitTerm_operator(self)
            else:
                return visitor.visitChildren(self)




    def term_operator(self):

        localctx = baby_duck_grammarParser.Term_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_term_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            _la = self._input.LA(1)
            if not(_la==33 or _la==34):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parenthesized_expression(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.Parenthesized_expressionContext,0)


        def ID(self):
            return self.getToken(baby_duck_grammarParser.ID, 0)

        def cte(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.CteContext,0)


        def factor_operator(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.Factor_operatorContext,0)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = baby_duck_grammarParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 238
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.parenthesized_expression()
                pass
            elif token in [31, 32, 35, 36, 38]:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==31 or _la==32:
                    self.state = 231
                    self.factor_operator()


                self.state = 236
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [35]:
                    self.state = 234
                    self.match(baby_duck_grammarParser.ID)
                    pass
                elif token in [36, 38]:
                    self.state = 235
                    self.cte()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Factor_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_factor_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor_operator" ):
                listener.enterFactor_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor_operator" ):
                listener.exitFactor_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor_operator" ):
                return visitor.visitFactor_operator(self)
            else:
                return visitor.visitChildren(self)




    def factor_operator(self):

        localctx = baby_duck_grammarParser.Factor_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_factor_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            _la = self._input.LA(1)
            if not(_la==31 or _la==32):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parenthesized_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_parenthesized_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesized_expression" ):
                listener.enterParenthesized_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesized_expression" ):
                listener.exitParenthesized_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesized_expression" ):
                return visitor.visitParenthesized_expression(self)
            else:
                return visitor.visitChildren(self)




    def parenthesized_expression(self):

        localctx = baby_duck_grammarParser.Parenthesized_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_parenthesized_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(baby_duck_grammarParser.T__19)
            self.state = 243
            self.expression()
            self.state = 244
            self.match(baby_duck_grammarParser.T__20)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class F_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(baby_duck_grammarParser.ID, 0)

        def f_call_helper(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.F_call_helperContext,0)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_f_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterF_call" ):
                listener.enterF_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitF_call" ):
                listener.exitF_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitF_call" ):
                return visitor.visitF_call(self)
            else:
                return visitor.visitChildren(self)




    def f_call(self):

        localctx = baby_duck_grammarParser.F_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_f_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(baby_duck_grammarParser.ID)
            self.state = 247
            self.match(baby_duck_grammarParser.T__19)
            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 384400621568) != 0):
                self.state = 248
                self.f_call_helper()


            self.state = 251
            self.match(baby_duck_grammarParser.T__20)
            self.state = 252
            self.match(baby_duck_grammarParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class F_call_helperContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(baby_duck_grammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(baby_duck_grammarParser.ExpressionContext,i)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_f_call_helper

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterF_call_helper" ):
                listener.enterF_call_helper(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitF_call_helper" ):
                listener.exitF_call_helper(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitF_call_helper" ):
                return visitor.visitF_call_helper(self)
            else:
                return visitor.visitChildren(self)




    def f_call_helper(self):

        localctx = baby_duck_grammarParser.F_call_helperContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_f_call_helper)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.expression()
            self.state = 259
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 255
                self.match(baby_duck_grammarParser.T__21)
                self.state = 256
                self.expression()
                self.state = 261
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





