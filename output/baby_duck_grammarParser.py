# Generated from baby_duck_grammar.g4 by ANTLR 4.13.0
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
        4,1,35,247,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,1,0,1,0,1,0,1,0,3,0,61,8,0,1,0,1,0,1,1,5,1,66,8,1,10,1,
        12,1,69,9,1,1,1,1,1,1,1,1,1,1,2,1,2,5,2,77,8,2,10,2,12,2,80,9,2,
        1,2,1,2,1,3,1,3,1,3,1,3,1,3,3,3,89,8,3,1,4,1,4,1,5,1,5,1,5,1,5,1,
        5,1,6,1,6,1,6,1,6,3,6,102,8,6,1,7,1,7,1,8,1,8,1,9,1,9,1,9,3,9,111,
        8,9,1,9,1,9,1,9,1,10,1,10,3,10,118,8,10,1,10,1,10,1,10,3,10,123,
        8,10,5,10,125,8,10,10,10,12,10,128,9,10,1,11,1,11,1,11,5,11,133,
        8,11,10,11,12,11,136,9,11,3,11,138,8,11,1,12,1,12,1,12,1,12,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,3,13,151,8,13,1,13,1,13,1,13,1,13,
        1,14,1,14,4,14,159,8,14,11,14,12,14,160,1,15,1,15,1,15,5,15,166,
        8,15,10,15,12,15,169,9,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,3,17,189,8,17,
        1,17,1,17,1,18,1,18,1,18,1,19,1,19,1,20,1,20,1,20,1,20,5,20,202,
        8,20,10,20,12,20,205,9,20,1,21,1,21,1,21,1,21,3,21,211,8,21,1,22,
        1,22,1,23,1,23,3,23,217,8,23,1,23,1,23,3,23,221,8,23,3,23,223,8,
        23,1,24,1,24,1,25,1,25,1,25,1,25,1,26,1,26,1,26,3,26,234,8,26,1,
        26,1,26,1,26,1,27,1,27,1,27,5,27,242,8,27,10,27,12,27,245,9,27,1,
        27,0,0,28,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,46,48,50,52,54,0,5,1,0,7,10,1,0,12,14,2,0,32,32,34,34,1,
        0,27,28,1,0,29,30,243,0,56,1,0,0,0,2,67,1,0,0,0,4,74,1,0,0,0,6,88,
        1,0,0,0,8,90,1,0,0,0,10,92,1,0,0,0,12,97,1,0,0,0,14,103,1,0,0,0,
        16,105,1,0,0,0,18,107,1,0,0,0,20,117,1,0,0,0,22,137,1,0,0,0,24,139,
        1,0,0,0,26,143,1,0,0,0,28,156,1,0,0,0,30,162,1,0,0,0,32,174,1,0,
        0,0,34,182,1,0,0,0,36,192,1,0,0,0,38,195,1,0,0,0,40,197,1,0,0,0,
        42,206,1,0,0,0,44,212,1,0,0,0,46,222,1,0,0,0,48,224,1,0,0,0,50,226,
        1,0,0,0,52,230,1,0,0,0,54,238,1,0,0,0,56,57,5,1,0,0,57,58,5,31,0,
        0,58,60,5,2,0,0,59,61,3,28,14,0,60,59,1,0,0,0,60,61,1,0,0,0,61,62,
        1,0,0,0,62,63,3,2,1,0,63,1,1,0,0,0,64,66,3,26,13,0,65,64,1,0,0,0,
        66,69,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,70,1,0,0,0,69,67,1,
        0,0,0,70,71,5,3,0,0,71,72,3,4,2,0,72,73,5,4,0,0,73,3,1,0,0,0,74,
        78,5,5,0,0,75,77,3,6,3,0,76,75,1,0,0,0,77,80,1,0,0,0,78,76,1,0,0,
        0,78,79,1,0,0,0,79,81,1,0,0,0,80,78,1,0,0,0,81,82,5,6,0,0,82,5,1,
        0,0,0,83,89,3,10,5,0,84,89,3,34,17,0,85,89,3,32,16,0,86,89,3,52,
        26,0,87,89,3,18,9,0,88,83,1,0,0,0,88,84,1,0,0,0,88,85,1,0,0,0,88,
        86,1,0,0,0,88,87,1,0,0,0,89,7,1,0,0,0,90,91,7,0,0,0,91,9,1,0,0,0,
        92,93,5,31,0,0,93,94,5,11,0,0,94,95,3,12,6,0,95,96,5,2,0,0,96,11,
        1,0,0,0,97,101,3,40,20,0,98,99,3,14,7,0,99,100,3,40,20,0,100,102,
        1,0,0,0,101,98,1,0,0,0,101,102,1,0,0,0,102,13,1,0,0,0,103,104,7,
        1,0,0,104,15,1,0,0,0,105,106,7,2,0,0,106,17,1,0,0,0,107,108,5,15,
        0,0,108,110,5,16,0,0,109,111,3,20,10,0,110,109,1,0,0,0,110,111,1,
        0,0,0,111,112,1,0,0,0,112,113,5,17,0,0,113,114,5,2,0,0,114,19,1,
        0,0,0,115,118,3,12,6,0,116,118,5,35,0,0,117,115,1,0,0,0,117,116,
        1,0,0,0,118,126,1,0,0,0,119,122,5,18,0,0,120,123,3,12,6,0,121,123,
        5,35,0,0,122,120,1,0,0,0,122,121,1,0,0,0,123,125,1,0,0,0,124,119,
        1,0,0,0,125,128,1,0,0,0,126,124,1,0,0,0,126,127,1,0,0,0,127,21,1,
        0,0,0,128,126,1,0,0,0,129,134,3,24,12,0,130,131,5,18,0,0,131,133,
        3,24,12,0,132,130,1,0,0,0,133,136,1,0,0,0,134,132,1,0,0,0,134,135,
        1,0,0,0,135,138,1,0,0,0,136,134,1,0,0,0,137,129,1,0,0,0,137,138,
        1,0,0,0,138,23,1,0,0,0,139,140,5,31,0,0,140,141,5,19,0,0,141,142,
        3,8,4,0,142,25,1,0,0,0,143,144,3,8,4,0,144,145,5,31,0,0,145,146,
        5,16,0,0,146,147,3,22,11,0,147,148,5,17,0,0,148,150,5,20,0,0,149,
        151,3,28,14,0,150,149,1,0,0,0,150,151,1,0,0,0,151,152,1,0,0,0,152,
        153,3,4,2,0,153,154,5,21,0,0,154,155,5,2,0,0,155,27,1,0,0,0,156,
        158,5,22,0,0,157,159,3,30,15,0,158,157,1,0,0,0,159,160,1,0,0,0,160,
        158,1,0,0,0,160,161,1,0,0,0,161,29,1,0,0,0,162,167,5,31,0,0,163,
        164,5,18,0,0,164,166,5,31,0,0,165,163,1,0,0,0,166,169,1,0,0,0,167,
        165,1,0,0,0,167,168,1,0,0,0,168,170,1,0,0,0,169,167,1,0,0,0,170,
        171,5,19,0,0,171,172,3,8,4,0,172,173,5,2,0,0,173,31,1,0,0,0,174,
        175,5,23,0,0,175,176,3,4,2,0,176,177,5,24,0,0,177,178,5,16,0,0,178,
        179,3,12,6,0,179,180,5,17,0,0,180,181,5,2,0,0,181,33,1,0,0,0,182,
        183,5,25,0,0,183,184,5,16,0,0,184,185,3,12,6,0,185,186,5,17,0,0,
        186,188,3,4,2,0,187,189,3,36,18,0,188,187,1,0,0,0,188,189,1,0,0,
        0,189,190,1,0,0,0,190,191,5,2,0,0,191,35,1,0,0,0,192,193,5,26,0,
        0,193,194,3,4,2,0,194,37,1,0,0,0,195,196,7,3,0,0,196,39,1,0,0,0,
        197,203,3,42,21,0,198,199,3,38,19,0,199,200,3,42,21,0,200,202,1,
        0,0,0,201,198,1,0,0,0,202,205,1,0,0,0,203,201,1,0,0,0,203,204,1,
        0,0,0,204,41,1,0,0,0,205,203,1,0,0,0,206,210,3,46,23,0,207,208,3,
        44,22,0,208,209,3,46,23,0,209,211,1,0,0,0,210,207,1,0,0,0,210,211,
        1,0,0,0,211,43,1,0,0,0,212,213,7,4,0,0,213,45,1,0,0,0,214,223,3,
        50,25,0,215,217,3,48,24,0,216,215,1,0,0,0,216,217,1,0,0,0,217,220,
        1,0,0,0,218,221,5,31,0,0,219,221,3,16,8,0,220,218,1,0,0,0,220,219,
        1,0,0,0,221,223,1,0,0,0,222,214,1,0,0,0,222,216,1,0,0,0,223,47,1,
        0,0,0,224,225,7,3,0,0,225,49,1,0,0,0,226,227,5,16,0,0,227,228,3,
        12,6,0,228,229,5,17,0,0,229,51,1,0,0,0,230,231,5,31,0,0,231,233,
        5,16,0,0,232,234,3,54,27,0,233,232,1,0,0,0,233,234,1,0,0,0,234,235,
        1,0,0,0,235,236,5,17,0,0,236,237,5,2,0,0,237,53,1,0,0,0,238,243,
        3,12,6,0,239,240,5,18,0,0,240,242,3,12,6,0,241,239,1,0,0,0,242,245,
        1,0,0,0,243,241,1,0,0,0,243,244,1,0,0,0,244,55,1,0,0,0,245,243,1,
        0,0,0,22,60,67,78,88,101,110,117,122,126,134,137,150,160,167,188,
        203,210,216,220,222,233,243
    ]

class baby_duck_grammarParser ( Parser ):

    grammarFileName = "baby_duck_grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "';'", "'main'", "'end'", 
                     "'{'", "'}'", "'int'", "'float'", "'bool'", "'void'", 
                     "'='", "'<'", "'>'", "'!='", "'print'", "'('", "')'", 
                     "','", "':'", "'['", "']'", "'var'", "'while'", "'do'", 
                     "'if'", "'else'", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "INT", 
                      "WS", "FLOAT", "STRING" ]

    RULE_program = 0
    RULE_program_post_var = 1
    RULE_body = 2
    RULE_statement = 3
    RULE_type = 4
    RULE_assign = 5
    RULE_expression = 6
    RULE_rel_op = 7
    RULE_cte = 8
    RULE_print = 9
    RULE_print_helper = 10
    RULE_f_param_list = 11
    RULE_f_param_list_helper = 12
    RULE_funcs = 13
    RULE_vars = 14
    RULE_vars_declarations = 15
    RULE_cycle = 16
    RULE_condition = 17
    RULE_condition_else = 18
    RULE_operator = 19
    RULE_exp = 20
    RULE_term = 21
    RULE_term_operator = 22
    RULE_factor = 23
    RULE_factor_operator = 24
    RULE_parenthesized_expression = 25
    RULE_f_call = 26
    RULE_f_call_helper = 27

    ruleNames =  [ "program", "program_post_var", "body", "statement", "type", 
                   "assign", "expression", "rel_op", "cte", "print", "print_helper", 
                   "f_param_list", "f_param_list_helper", "funcs", "vars", 
                   "vars_declarations", "cycle", "condition", "condition_else", 
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
    ID=31
    INT=32
    WS=33
    FLOAT=34
    STRING=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




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
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(baby_duck_grammarParser.T__0)
            self.state = 57
            self.match(baby_duck_grammarParser.ID)
            self.state = 58
            self.match(baby_duck_grammarParser.T__1)
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 59
                self.vars_()


            self.state = 62
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
        self.enterRule(localctx, 2, self.RULE_program_post_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1920) != 0):
                self.state = 64
                self.funcs()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 70
            self.match(baby_duck_grammarParser.T__2)
            self.state = 71
            self.body()
            self.state = 72
            self.match(baby_duck_grammarParser.T__3)
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
        self.enterRule(localctx, 4, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(baby_duck_grammarParser.T__4)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2189459456) != 0):
                self.state = 75
                self.statement()
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 81
            self.match(baby_duck_grammarParser.T__5)
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
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.assign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.condition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 85
                self.cycle()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 86
                self.f_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 87
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
        self.enterRule(localctx, 8, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1920) != 0)):
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
        self.enterRule(localctx, 10, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(baby_duck_grammarParser.ID)
            self.state = 93
            self.match(baby_duck_grammarParser.T__10)
            self.state = 94
            self.expression()
            self.state = 95
            self.match(baby_duck_grammarParser.T__1)
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

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(baby_duck_grammarParser.ExpContext)
            else:
                return self.getTypedRuleContext(baby_duck_grammarParser.ExpContext,i)


        def rel_op(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.Rel_opContext,0)


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
        self.enterRule(localctx, 12, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.exp()
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 28672) != 0):
                self.state = 98
                self.rel_op()
                self.state = 99
                self.exp()


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
        self.enterRule(localctx, 14, self.RULE_rel_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 28672) != 0)):
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
        self.enterRule(localctx, 16, self.RULE_cte)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            _la = self._input.LA(1)
            if not(_la==32 or _la==34):
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
        self.enterRule(localctx, 18, self.RULE_print)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(baby_duck_grammarParser.T__14)
            self.state = 108
            self.match(baby_duck_grammarParser.T__15)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 58384777216) != 0):
                self.state = 109
                self.print_helper()


            self.state = 112
            self.match(baby_duck_grammarParser.T__16)
            self.state = 113
            self.match(baby_duck_grammarParser.T__1)
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


        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(baby_duck_grammarParser.STRING)
            else:
                return self.getToken(baby_duck_grammarParser.STRING, i)

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
        self.enterRule(localctx, 20, self.RULE_print_helper)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16, 27, 28, 31, 32, 34]:
                self.state = 115
                self.expression()
                pass
            elif token in [35]:
                self.state = 116
                self.match(baby_duck_grammarParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 119
                self.match(baby_duck_grammarParser.T__17)
                self.state = 122
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [16, 27, 28, 31, 32, 34]:
                    self.state = 120
                    self.expression()
                    pass
                elif token in [35]:
                    self.state = 121
                    self.match(baby_duck_grammarParser.STRING)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 128
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
        self.enterRule(localctx, 22, self.RULE_f_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 129
                self.f_param_list_helper()
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==18:
                    self.state = 130
                    self.match(baby_duck_grammarParser.T__17)
                    self.state = 131
                    self.f_param_list_helper()
                    self.state = 136
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
        self.enterRule(localctx, 24, self.RULE_f_param_list_helper)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(baby_duck_grammarParser.ID)
            self.state = 140
            self.match(baby_duck_grammarParser.T__18)
            self.state = 141
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

        def type_(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.TypeContext,0)


        def ID(self):
            return self.getToken(baby_duck_grammarParser.ID, 0)

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
        self.enterRule(localctx, 26, self.RULE_funcs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.type_()
            self.state = 144
            self.match(baby_duck_grammarParser.ID)
            self.state = 145
            self.match(baby_duck_grammarParser.T__15)
            self.state = 146
            self.f_param_list()
            self.state = 147
            self.match(baby_duck_grammarParser.T__16)
            self.state = 148
            self.match(baby_duck_grammarParser.T__19)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 149
                self.vars_()


            self.state = 152
            self.body()
            self.state = 153
            self.match(baby_duck_grammarParser.T__20)
            self.state = 154
            self.match(baby_duck_grammarParser.T__1)
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
        self.enterRule(localctx, 28, self.RULE_vars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(baby_duck_grammarParser.T__21)
            self.state = 158 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 157
                self.vars_declarations()
                self.state = 160 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==31):
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
        self.enterRule(localctx, 30, self.RULE_vars_declarations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(baby_duck_grammarParser.ID)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 163
                self.match(baby_duck_grammarParser.T__17)
                self.state = 164
                self.match(baby_duck_grammarParser.ID)
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 170
            self.match(baby_duck_grammarParser.T__18)
            self.state = 171
            self.type_()
            self.state = 172
            self.match(baby_duck_grammarParser.T__1)
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
        self.enterRule(localctx, 32, self.RULE_cycle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(baby_duck_grammarParser.T__22)
            self.state = 175
            self.body()
            self.state = 176
            self.match(baby_duck_grammarParser.T__23)
            self.state = 177
            self.match(baby_duck_grammarParser.T__15)
            self.state = 178
            self.expression()
            self.state = 179
            self.match(baby_duck_grammarParser.T__16)
            self.state = 180
            self.match(baby_duck_grammarParser.T__1)
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
        self.enterRule(localctx, 34, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(baby_duck_grammarParser.T__24)
            self.state = 183
            self.match(baby_duck_grammarParser.T__15)
            self.state = 184
            self.expression()
            self.state = 185
            self.match(baby_duck_grammarParser.T__16)
            self.state = 186
            self.body()
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 187
                self.condition_else()


            self.state = 190
            self.match(baby_duck_grammarParser.T__1)
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
        self.enterRule(localctx, 36, self.RULE_condition_else)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(baby_duck_grammarParser.T__25)
            self.state = 193
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
        self.enterRule(localctx, 38, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            _la = self._input.LA(1)
            if not(_la==27 or _la==28):
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

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(baby_duck_grammarParser.TermContext)
            else:
                return self.getTypedRuleContext(baby_duck_grammarParser.TermContext,i)


        def operator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(baby_duck_grammarParser.OperatorContext)
            else:
                return self.getTypedRuleContext(baby_duck_grammarParser.OperatorContext,i)


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
        self.enterRule(localctx, 40, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.term()
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27 or _la==28:
                self.state = 198
                self.operator()
                self.state = 199
                self.term()
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(baby_duck_grammarParser.FactorContext)
            else:
                return self.getTypedRuleContext(baby_duck_grammarParser.FactorContext,i)


        def term_operator(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.Term_operatorContext,0)


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
        self.enterRule(localctx, 42, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.factor()
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29 or _la==30:
                self.state = 207
                self.term_operator()
                self.state = 208
                self.factor()


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
        self.enterRule(localctx, 44, self.RULE_term_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            _la = self._input.LA(1)
            if not(_la==29 or _la==30):
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
        self.enterRule(localctx, 46, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 222
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.parenthesized_expression()
                pass
            elif token in [27, 28, 31, 32, 34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==27 or _la==28:
                    self.state = 215
                    self.factor_operator()


                self.state = 220
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [31]:
                    self.state = 218
                    self.match(baby_duck_grammarParser.ID)
                    pass
                elif token in [32, 34]:
                    self.state = 219
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
        self.enterRule(localctx, 48, self.RULE_factor_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            _la = self._input.LA(1)
            if not(_la==27 or _la==28):
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
        self.enterRule(localctx, 50, self.RULE_parenthesized_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(baby_duck_grammarParser.T__15)
            self.state = 227
            self.expression()
            self.state = 228
            self.match(baby_duck_grammarParser.T__16)
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
        self.enterRule(localctx, 52, self.RULE_f_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(baby_duck_grammarParser.ID)
            self.state = 231
            self.match(baby_duck_grammarParser.T__15)
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 24025038848) != 0):
                self.state = 232
                self.f_call_helper()


            self.state = 235
            self.match(baby_duck_grammarParser.T__16)
            self.state = 236
            self.match(baby_duck_grammarParser.T__1)
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
        self.enterRule(localctx, 54, self.RULE_f_call_helper)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.expression()
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 239
                self.match(baby_duck_grammarParser.T__17)
                self.state = 240
                self.expression()
                self.state = 245
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





