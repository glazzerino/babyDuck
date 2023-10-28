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
        4,1,35,230,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,1,0,1,0,1,0,3,0,53,8,0,1,
        0,1,0,1,1,5,1,58,8,1,10,1,12,1,61,9,1,1,1,1,1,1,1,1,1,1,2,1,2,5,
        2,69,8,2,10,2,12,2,72,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,3,3,81,8,3,
        1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,3,6,94,8,6,1,7,1,7,1,
        8,1,8,1,9,1,9,1,9,5,9,103,8,9,10,9,12,9,106,9,9,1,10,1,10,1,10,3,
        10,111,8,10,1,10,1,10,1,10,1,11,1,11,3,11,118,8,11,1,11,1,11,1,11,
        3,11,123,8,11,5,11,125,8,11,10,11,12,11,128,9,11,1,12,1,12,1,12,
        5,12,133,8,12,10,12,12,12,136,9,12,3,12,138,8,12,1,13,1,13,1,13,
        1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,151,8,14,1,14,1,14,
        1,14,1,14,1,15,1,15,4,15,159,8,15,11,15,12,15,160,1,16,1,16,1,16,
        5,16,166,8,16,10,16,12,16,169,9,16,1,16,1,16,1,16,1,16,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,3,18,
        189,8,18,1,18,1,18,1,19,1,19,1,19,1,20,1,20,1,20,3,20,199,8,20,1,
        21,1,21,1,21,1,21,1,21,3,21,206,8,21,1,21,1,21,3,21,210,8,21,3,21,
        212,8,21,1,22,1,22,1,22,3,22,217,8,22,1,22,1,22,1,22,1,23,1,23,1,
        23,5,23,225,8,23,10,23,12,23,228,9,23,1,23,0,0,24,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,0,5,1,0,7,10,
        1,0,12,14,2,0,32,32,34,34,1,0,15,16,1,0,29,30,230,0,48,1,0,0,0,2,
        59,1,0,0,0,4,66,1,0,0,0,6,80,1,0,0,0,8,82,1,0,0,0,10,84,1,0,0,0,
        12,89,1,0,0,0,14,95,1,0,0,0,16,97,1,0,0,0,18,99,1,0,0,0,20,107,1,
        0,0,0,22,117,1,0,0,0,24,137,1,0,0,0,26,139,1,0,0,0,28,143,1,0,0,
        0,30,156,1,0,0,0,32,162,1,0,0,0,34,174,1,0,0,0,36,182,1,0,0,0,38,
        192,1,0,0,0,40,195,1,0,0,0,42,211,1,0,0,0,44,213,1,0,0,0,46,221,
        1,0,0,0,48,49,5,1,0,0,49,50,5,31,0,0,50,52,5,2,0,0,51,53,3,30,15,
        0,52,51,1,0,0,0,52,53,1,0,0,0,53,54,1,0,0,0,54,55,3,2,1,0,55,1,1,
        0,0,0,56,58,3,28,14,0,57,56,1,0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,
        59,60,1,0,0,0,60,62,1,0,0,0,61,59,1,0,0,0,62,63,5,3,0,0,63,64,3,
        4,2,0,64,65,5,4,0,0,65,3,1,0,0,0,66,70,5,5,0,0,67,69,3,6,3,0,68,
        67,1,0,0,0,69,72,1,0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,73,1,0,0,
        0,72,70,1,0,0,0,73,74,5,6,0,0,74,5,1,0,0,0,75,81,3,10,5,0,76,81,
        3,36,18,0,77,81,3,34,17,0,78,81,3,44,22,0,79,81,3,20,10,0,80,75,
        1,0,0,0,80,76,1,0,0,0,80,77,1,0,0,0,80,78,1,0,0,0,80,79,1,0,0,0,
        81,7,1,0,0,0,82,83,7,0,0,0,83,9,1,0,0,0,84,85,5,31,0,0,85,86,5,11,
        0,0,86,87,3,12,6,0,87,88,5,2,0,0,88,11,1,0,0,0,89,93,3,18,9,0,90,
        91,3,14,7,0,91,92,3,18,9,0,92,94,1,0,0,0,93,90,1,0,0,0,93,94,1,0,
        0,0,94,13,1,0,0,0,95,96,7,1,0,0,96,15,1,0,0,0,97,98,7,2,0,0,98,17,
        1,0,0,0,99,104,3,40,20,0,100,101,7,3,0,0,101,103,3,40,20,0,102,100,
        1,0,0,0,103,106,1,0,0,0,104,102,1,0,0,0,104,105,1,0,0,0,105,19,1,
        0,0,0,106,104,1,0,0,0,107,108,5,17,0,0,108,110,5,18,0,0,109,111,
        3,22,11,0,110,109,1,0,0,0,110,111,1,0,0,0,111,112,1,0,0,0,112,113,
        5,19,0,0,113,114,5,2,0,0,114,21,1,0,0,0,115,118,3,12,6,0,116,118,
        5,35,0,0,117,115,1,0,0,0,117,116,1,0,0,0,118,126,1,0,0,0,119,122,
        5,20,0,0,120,123,3,12,6,0,121,123,5,35,0,0,122,120,1,0,0,0,122,121,
        1,0,0,0,123,125,1,0,0,0,124,119,1,0,0,0,125,128,1,0,0,0,126,124,
        1,0,0,0,126,127,1,0,0,0,127,23,1,0,0,0,128,126,1,0,0,0,129,134,3,
        26,13,0,130,131,5,20,0,0,131,133,3,26,13,0,132,130,1,0,0,0,133,136,
        1,0,0,0,134,132,1,0,0,0,134,135,1,0,0,0,135,138,1,0,0,0,136,134,
        1,0,0,0,137,129,1,0,0,0,137,138,1,0,0,0,138,25,1,0,0,0,139,140,5,
        31,0,0,140,141,5,21,0,0,141,142,3,8,4,0,142,27,1,0,0,0,143,144,3,
        8,4,0,144,145,5,31,0,0,145,146,5,18,0,0,146,147,3,24,12,0,147,148,
        5,19,0,0,148,150,5,22,0,0,149,151,3,30,15,0,150,149,1,0,0,0,150,
        151,1,0,0,0,151,152,1,0,0,0,152,153,3,4,2,0,153,154,5,23,0,0,154,
        155,5,2,0,0,155,29,1,0,0,0,156,158,5,24,0,0,157,159,3,32,16,0,158,
        157,1,0,0,0,159,160,1,0,0,0,160,158,1,0,0,0,160,161,1,0,0,0,161,
        31,1,0,0,0,162,167,5,31,0,0,163,164,5,20,0,0,164,166,5,31,0,0,165,
        163,1,0,0,0,166,169,1,0,0,0,167,165,1,0,0,0,167,168,1,0,0,0,168,
        170,1,0,0,0,169,167,1,0,0,0,170,171,5,21,0,0,171,172,3,8,4,0,172,
        173,5,2,0,0,173,33,1,0,0,0,174,175,5,25,0,0,175,176,3,4,2,0,176,
        177,5,26,0,0,177,178,5,18,0,0,178,179,3,12,6,0,179,180,5,19,0,0,
        180,181,5,2,0,0,181,35,1,0,0,0,182,183,5,27,0,0,183,184,5,18,0,0,
        184,185,3,12,6,0,185,186,5,19,0,0,186,188,3,4,2,0,187,189,3,38,19,
        0,188,187,1,0,0,0,188,189,1,0,0,0,189,190,1,0,0,0,190,191,5,2,0,
        0,191,37,1,0,0,0,192,193,5,28,0,0,193,194,3,4,2,0,194,39,1,0,0,0,
        195,198,3,42,21,0,196,197,7,4,0,0,197,199,3,42,21,0,198,196,1,0,
        0,0,198,199,1,0,0,0,199,41,1,0,0,0,200,201,5,18,0,0,201,202,3,12,
        6,0,202,203,5,19,0,0,203,212,1,0,0,0,204,206,7,3,0,0,205,204,1,0,
        0,0,205,206,1,0,0,0,206,209,1,0,0,0,207,210,5,31,0,0,208,210,3,16,
        8,0,209,207,1,0,0,0,209,208,1,0,0,0,210,212,1,0,0,0,211,200,1,0,
        0,0,211,205,1,0,0,0,212,43,1,0,0,0,213,214,5,31,0,0,214,216,5,18,
        0,0,215,217,3,46,23,0,216,215,1,0,0,0,216,217,1,0,0,0,217,218,1,
        0,0,0,218,219,5,19,0,0,219,220,5,2,0,0,220,45,1,0,0,0,221,226,3,
        12,6,0,222,223,5,20,0,0,223,225,3,12,6,0,224,222,1,0,0,0,225,228,
        1,0,0,0,226,224,1,0,0,0,226,227,1,0,0,0,227,47,1,0,0,0,228,226,1,
        0,0,0,22,52,59,70,80,93,104,110,117,122,126,134,137,150,160,167,
        188,198,205,209,211,216,226
    ]

class baby_duck_grammarParser ( Parser ):

    grammarFileName = "baby_duck_grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "';'", "'main'", "'end'", 
                     "'{'", "'}'", "'int'", "'float'", "'bool'", "'void'", 
                     "'='", "'<'", "'>'", "'!='", "'+'", "'-'", "'print'", 
                     "'('", "')'", "','", "':'", "'['", "']'", "'var'", 
                     "'while'", "'do'", "'if'", "'else'", "'*'", "'/'" ]

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
    RULE_exp = 9
    RULE_print = 10
    RULE_print_helper = 11
    RULE_f_param_list = 12
    RULE_f_param_list_helper = 13
    RULE_funcs = 14
    RULE_vars = 15
    RULE_vars_declarations = 16
    RULE_cycle = 17
    RULE_condition = 18
    RULE_condition_else = 19
    RULE_term = 20
    RULE_factor = 21
    RULE_f_call = 22
    RULE_f_call_helper = 23

    ruleNames =  [ "program", "program_post_var", "body", "statement", "type", 
                   "assign", "expression", "rel_op", "cte", "exp", "print", 
                   "print_helper", "f_param_list", "f_param_list_helper", 
                   "funcs", "vars", "vars_declarations", "cycle", "condition", 
                   "condition_else", "term", "factor", "f_call", "f_call_helper" ]

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




    def program(self):

        localctx = baby_duck_grammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(baby_duck_grammarParser.T__0)
            self.state = 49
            self.match(baby_duck_grammarParser.ID)
            self.state = 50
            self.match(baby_duck_grammarParser.T__1)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 51
                self.vars_()


            self.state = 54
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




    def program_post_var(self):

        localctx = baby_duck_grammarParser.Program_post_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_program_post_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1920) != 0):
                self.state = 56
                self.funcs()
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 62
            self.match(baby_duck_grammarParser.T__2)
            self.state = 63
            self.body()
            self.state = 64
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




    def body(self):

        localctx = baby_duck_grammarParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(baby_duck_grammarParser.T__4)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2315386880) != 0):
                self.state = 67
                self.statement()
                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 73
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




    def statement(self):

        localctx = baby_duck_grammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 80
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.assign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.condition()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 77
                self.cycle()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 78
                self.f_call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 79
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




    def type_(self):

        localctx = baby_duck_grammarParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
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




    def assign(self):

        localctx = baby_duck_grammarParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(baby_duck_grammarParser.ID)
            self.state = 85
            self.match(baby_duck_grammarParser.T__10)
            self.state = 86
            self.expression()
            self.state = 87
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




    def expression(self):

        localctx = baby_duck_grammarParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.exp()
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 28672) != 0):
                self.state = 90
                self.rel_op()
                self.state = 91
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




    def rel_op(self):

        localctx = baby_duck_grammarParser.Rel_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_rel_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
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




    def cte(self):

        localctx = baby_duck_grammarParser.CteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_cte)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
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


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)




    def exp(self):

        localctx = baby_duck_grammarParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.term()
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15 or _la==16:
                self.state = 100
                _la = self._input.LA(1)
                if not(_la==15 or _la==16):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 101
                self.term()
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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




    def print_(self):

        localctx = baby_duck_grammarParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_print)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(baby_duck_grammarParser.T__16)
            self.state = 108
            self.match(baby_duck_grammarParser.T__17)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 57982418944) != 0):
                self.state = 109
                self.print_helper()


            self.state = 112
            self.match(baby_duck_grammarParser.T__18)
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




    def print_helper(self):

        localctx = baby_duck_grammarParser.Print_helperContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_print_helper)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15, 16, 18, 31, 32, 34]:
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
            while _la==20:
                self.state = 119
                self.match(baby_duck_grammarParser.T__19)
                self.state = 122
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [15, 16, 18, 31, 32, 34]:
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




    def f_param_list(self):

        localctx = baby_duck_grammarParser.F_param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_f_param_list)
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
                while _la==20:
                    self.state = 130
                    self.match(baby_duck_grammarParser.T__19)
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




    def f_param_list_helper(self):

        localctx = baby_duck_grammarParser.F_param_list_helperContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_f_param_list_helper)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(baby_duck_grammarParser.ID)
            self.state = 140
            self.match(baby_duck_grammarParser.T__20)
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




    def funcs(self):

        localctx = baby_duck_grammarParser.FuncsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_funcs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.type_()
            self.state = 144
            self.match(baby_duck_grammarParser.ID)
            self.state = 145
            self.match(baby_duck_grammarParser.T__17)
            self.state = 146
            self.f_param_list()
            self.state = 147
            self.match(baby_duck_grammarParser.T__18)
            self.state = 148
            self.match(baby_duck_grammarParser.T__21)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 149
                self.vars_()


            self.state = 152
            self.body()
            self.state = 153
            self.match(baby_duck_grammarParser.T__22)
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




    def vars_(self):

        localctx = baby_duck_grammarParser.VarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_vars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(baby_duck_grammarParser.T__23)
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




    def vars_declarations(self):

        localctx = baby_duck_grammarParser.Vars_declarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_vars_declarations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(baby_duck_grammarParser.ID)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 163
                self.match(baby_duck_grammarParser.T__19)
                self.state = 164
                self.match(baby_duck_grammarParser.ID)
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 170
            self.match(baby_duck_grammarParser.T__20)
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




    def cycle(self):

        localctx = baby_duck_grammarParser.CycleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_cycle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(baby_duck_grammarParser.T__24)
            self.state = 175
            self.body()
            self.state = 176
            self.match(baby_duck_grammarParser.T__25)
            self.state = 177
            self.match(baby_duck_grammarParser.T__17)
            self.state = 178
            self.expression()
            self.state = 179
            self.match(baby_duck_grammarParser.T__18)
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




    def condition(self):

        localctx = baby_duck_grammarParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(baby_duck_grammarParser.T__26)
            self.state = 183
            self.match(baby_duck_grammarParser.T__17)
            self.state = 184
            self.expression()
            self.state = 185
            self.match(baby_duck_grammarParser.T__18)
            self.state = 186
            self.body()
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
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




    def condition_else(self):

        localctx = baby_duck_grammarParser.Condition_elseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_condition_else)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(baby_duck_grammarParser.T__27)
            self.state = 193
            self.body()
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


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = baby_duck_grammarParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.factor()
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29 or _la==30:
                self.state = 196
                _la = self._input.LA(1)
                if not(_la==29 or _la==30):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 197
                self.factor()


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

        def expression(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.ExpressionContext,0)


        def ID(self):
            return self.getToken(baby_duck_grammarParser.ID, 0)

        def cte(self):
            return self.getTypedRuleContext(baby_duck_grammarParser.CteContext,0)


        def getRuleIndex(self):
            return baby_duck_grammarParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = baby_duck_grammarParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.state = 211
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.match(baby_duck_grammarParser.T__17)
                self.state = 201
                self.expression()
                self.state = 202
                self.match(baby_duck_grammarParser.T__18)
                pass
            elif token in [15, 16, 31, 32, 34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==15 or _la==16:
                    self.state = 204
                    _la = self._input.LA(1)
                    if not(_la==15 or _la==16):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 209
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [31]:
                    self.state = 207
                    self.match(baby_duck_grammarParser.ID)
                    pass
                elif token in [32, 34]:
                    self.state = 208
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




    def f_call(self):

        localctx = baby_duck_grammarParser.F_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_f_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(baby_duck_grammarParser.ID)
            self.state = 214
            self.match(baby_duck_grammarParser.T__17)
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 23622680576) != 0):
                self.state = 215
                self.f_call_helper()


            self.state = 218
            self.match(baby_duck_grammarParser.T__18)
            self.state = 219
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




    def f_call_helper(self):

        localctx = baby_duck_grammarParser.F_call_helperContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_f_call_helper)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.expression()
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 222
                self.match(baby_duck_grammarParser.T__19)
                self.state = 223
                self.expression()
                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





