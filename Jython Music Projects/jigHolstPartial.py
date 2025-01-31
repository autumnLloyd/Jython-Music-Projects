# jigHolstPartial.py
#
# Author:  Autumn R. Lloyd
# Email:   lloydar@g.cofc.edu
# Class:   FYSE 112-01   
# Assignment: Homework #2
# Due Date:  29 September 2022 
#
# Purpose: excerpt from the Jig in St Paul's Suite
#          originally composed by Holst. I have arranged the piece to be
#          slightly shorter.

from music import *

#creating score, bpm is En = 167 
stPaulJigScore = Score("Jig from Saint Paul's Suite" , 250) 

#establishing parts
violinOnePart  =  Part(VIOLIN, 0)
violinTwoPart  =  Part(VIOLIN, 1)
violaPart      =  Part(VIOLA, 2)
celloPart      =  Part(CELLO, 3)
doubleBassPart =  Part(DOUBLE_BASS, 4)

#establishing phrases

violinOnePhrase   = Phrase(0.0)
violinTwoPhrase   = Phrase(0.0)
violaPhrase       = Phrase(0.0)
celloPhrase       = Phrase(0.0)
doubleBassPhrase  = Phrase(0.0)

#actual musical stuff
melodyPitches     = [D4, E4, F4, F4,    E4, C4, D4, D4,   E4, F4, G4, F4, E4,  D4, D4, D4, 
              E4, F4, G4, G4,    A4, A4, E4, D4, C4,   D4, C4, B3, A3, G3,    A3, B3, C4, E4] 
melodyRhythm       = [QN, EN, QN, EN,    QN, EN, QN, EN,   QN, EN, EN, EN, EN,  DQN, QN, EN, 
              QN, EN, QN, EN,    QN, EN, EN, EN, EN,   QN, EN, EN, EN, EN,    QN, EN, QN, EN]
melodyUpOnePitches = [D5, E5, F5, F5,    E5, C5, D5, D5,   E5, F5, G5, F5, E5,  D5, D5, D5, 
              E5, F5, G5, G5,    A5, A5, E5, D5, C5,   D5, C5, B4, A4, G4,    A4, B4, C5, E5]

melodyDynamic = [FORTE] * 34          #duration of repeating melody
bassLineRest        = [REST] * 8      #8 measures of rest
bassBlock1RestDur   = [EN * 6 ] * 8   #in 6/8 time

block2UnisonPitch  = [D4,  D4,  E4,   C4,  A3, B3, C4, B3, A3,     D4,  D4,  E4,    F4, E4, D4, C4, B3, A3, G3]
block2UnisonRhythm = [DQN, DQN, DQN,  DQN, QN, EN, EN, EN, EN,     DQN, DQN, DQN,   QN, EN, QN, EN, EN, EN, EN]

bassBlock2RestDur = ([EN * 9] * 4) + ([EN * 6] * 4)   #8 measures of rest in 9/8 and 6/8 time

#essentially chords
block2Violin2Pitch  = [D4, C4, D4, D4,    C4, REST, D4, REST,    E4, REST, C4, REST,   B3,  B3, B3,
                         C4, REST, D4, REST,    E4, REST, REST, REST,   B3, REST, REST, REST,   A3, REST, REST, REST]
block2ViolaPitch    = [A3, G3, A3, B3,    C4, REST, A3, REST,    C4, REST, G3, REST,   G3,  G3, G3,
                         E4, REST, D4, REST,    C4, REST, REST, REST,   G3, REST, REST, REST,   F3, REST, REST, REST]
block2CelloPitch    = [F3, E3, D3, D3,    A3, REST, D3, REST,    C3, REST, E3, REST,   G3,  G3, G3,
                         C4, REST, B3, REST,    C4, REST, REST, REST,   G3, REST, REST, REST,   F3, REST, REST, REST]
block2UnisonRhythm2 = [QN, EN, QN, EN,    QN, EN,   QN, EN,      QN, EN,   QN, EN,     DQN, QN, EN,
                         QN, EN,   QN, EN,    QN,   EN,   QN,   EN,     QN, EN,   QN,   EN,     QN, EN,   QN,   EN]
                         
block3Violin1Pitch  = [D4,  D4,  E4,      C4,  A3, B3, C4, B3, A3,    D4,  D4,  E4,     F4, E4, D4, REST, REST, REST]
block3Violin1Rhythm  = [DQN, DQN, DQN,     DQN, QN, EN, EN, EN, EN,    DQN, DQN, DQN,    QN, EN, QN, EN,   QN,   EN]

block3Violin2Pitch  = [B4,  B4,  B4,     C4, REST, REST, REST,      B4,  B4,  C4,    D4, E4,   D4, C4, B3, A3, G3]
block3ViolaPitch    = [G3,  G3,  G3,     A3, REST, REST, REST,      G3,  G3,  G3,    A3, REST, D4, C4, B3, A3, G3]
block3UnisonRhythm  = [DQN, DQN, DQN,    QN, EN,   DQN,  DQN,       DQN, DQN, DQN,   QN, EN,   QN, EN, EN, EN, EN]

block3CelloPitch  = [G3,  G3,  E3,     A3, REST, REST, REST,   G3,  G3,  E3,     D3, REST, REST, G3, REST]
block3CelloRhythm = [DQN, DQN, DQN,    QN, EN,   DQN,  DQN,    DQN, DQN, DQN,    QN, EN,   DQN,  QN, EN]

block3BassRest    = [REST]     #lines up the bass part, idk why it works this way
block3BassRestDur = [EN * 9 ]  # timing is off somewhere but this compensates

block4ChordRhythm = [DQN, DQN] * 8 #8 measures of 6/8 in dotted quarter notes

block4Violin2Pitch    = [[A4, D4], [A4, D4],    E4,      [A4, D4],   E4,      C5,          [D4, B4], [D4, G3],
                           [G4, G3], [G4, G3],     [C5,E4], E4,   [A4, D4], E4,    F4,  E4]
block4ViolaPitch      = [ F4,       F4,          [G3,C3], F4,         [G3,C3], [G4,G3],     [G4,G3],  [G4,G3],
                           E4,       D4,           C4,      B3,   A3,       G3,    D4, [G3, C3]]
block4CelloPitch      = [[A3,D3], [A3, D3],    [G2, C2], [A3, D3],  [G2, C2], E3,           G2,       B2,
                           C3,       B2,           A2,      G2,   F2,       E2,    D2,  C2]
block4DoubleBassPitch = [A2,       A2,         G2,        A2,       G2,       B2,           D3,       F3,
                           G3,     F3,           E3,     D3,      C3,       B2,    A2,  G2]
block5Violin1Pitch  = [[G5, B4], [G5, B4], [A5, C5],   [F5, A4], REST, D4, E4, F4, E4, D4,    [G5, B4], [G5, B4], [A5, C5],    [F5, A4], REST, D4, E4, F4, E4, D4,
                         [G4, B3], [G4, B3], [A4, C4],   [F4, A3], [F4, A3], [G4, B3],    [E4, G3], [E4, G3], [F4, A3]]
block5Violin2Pitch = [[G4, B3], [G4, B3], [A4, C4],   [F4, A3], REST, D4, E4, F4, E4, D4,    [G4, B3], [G4, B3], [A4, C4],    [F4, A3], REST, D4, E4, F4, E4, D4,
                         [G4, B3], [G4, B3], [A4, C4],   [F4, A3], [F4, A3], [G4, B3],    [E4, G3], [E4, G3], [F4, A3]]
block5ViolaPitch   = [[B4, G3], [B4, G3], E3,          D3,      REST, D4, E4, F4, E4, D4,    [D4, G3], [D4, G3], E3,           D3,      REST, D4, E4, F4, E4, D4,
                         [D4, G3], [D4, G3], [E4, A3],   C4,        C4,      [D4, G3],    E3,       E3,        A3]                          
block5UpperRhythm  = [DQN,       DQN,        DQN,     QN,       EN,   QN, EN, EN, EN, EN,    DQN,     DQN,        DQN,         QN,      EN,   QN, EN, EN, EN, EN,
                         DQN,       DQN,      DQN,       DQN,       DQN,      DQN,        DQN,      DQN,       DQN]
block5CelloPitch      = [[D3, G2], [D3, G2], A2,      D2, REST, REST, REST,      [D3, G2], [D3, G2], A2,       D2, REST, REST, REST,
                           F3,  F3,  E3,     E3,  E3,  D3,     D3,  D3,  C3]
block5DoubleBassPitch = [G1,        G1,      A1,      D1, REST, REST, REST,       G1,       G1,      A1,       D1, REST, REST, REST,
                           F2,  F2,  E2,     E2,  E2,  D2,     D2,  D2,  C2]
block5LowerRhythm     = [DQN,      DQN,      DQN,    QN,  EN,   DQN,  DQN,        DQN,      DQN,     DQN,      QN, EN,   DQN,  DQN,
                           DQN, DQN, DQN,    DQN, DQN, DQN,    DQN, DQN, DQN]
block6Violin1Pitch = [D4,  D4,      [E4, G3], REST, [E4, G3], REST, [E4, G3], REST] * 2 #repeats
block6ViolaPitch   = [F3,  F3,      [G3, C3], REST, [G3, C3], REST, [G3, C3], REST] * 2
block6UpperRhythm  = [DHN, DQN,     QN,       EN,    QN,      EN,    QN,      EN]   * 2   

block6Violin2Pitch = [D4,  REST, BF3,   C4, D4, C4, BF4,     C4,  REST, C4,  REST, C4,  REST] *2  #repeats
block6CelloPitch   = [BF2, REST, BF2,   C3, D3, C3, BF2,     BF2, REST, BF2, REST, BF2, REST] *2
block6LowerRhythm  = [QN, EN,   QN,     EN, EN, EN, EN,      QN,  EN,   QN,  EN,   QN,  EN]   *2  

block6DoubleBassPitch  = [BF1, REST, REST, REST,      BF1, REST, BF1, REST, BF1, REST] *2  #repeats
block6DoubleBassRhythm = [QN,  EN,   DQN,  DQN,       QN,  EN,   QN,  EN,   QN,  EN]   *2

block7Violin1Pitch = [D4,  E4,  F4,  G4,   [A5, CS5], [E5, A4],  G4,        [A5, CS5],  E5,         G4,      [E5, A4],  A4,   E4]
block7Violin2Pitch = [BF3, C4,  D4,  E4,   [E5, A4],  [CS5, E4], [D4, G3],  [E5, A4],  [CS5, E4],  [D4, B3], [CS5, E4], E4,   D4]
block7ViolinRhythm = [DHN, DHN, DHN, DHN,   DQN,        DQN,     DHN,        DQN,       DQN,        DHN,      DQN,      DQN,  DHN]

block7ViolaPitch  = [BF3, C4, D4, C4, BF3,  BF3, C4, D4, C4, BF3,  BF3, C4, D4, C4, BF3,  BF3, C4, D4, C4, BF3,
                        A3, A3,     BF3, C4, D4, C4, BF3,   A3,  A3,      BF3, C4, D4, C4, BF3,    A3, CS4,       G3, A3, BF3, A3, G3]
block7CelloPitch  = [BF2, C3, D3, C3, BF2,  BF2, C3, D3, C3, BF2,  BF2, C3, D3, C3, BF2,  BF2, C3, D3, C3, BF2,
                        A2, A2,     BF2, C3, D3, C3, BF2,   A2,  A2,      BF2, C3, D3, C3, BF2,    A2, A2,        G2, A2, BF2, A2, G2]
block7LowerRhythm = [QN,  EN, EN, EN, EN,   QN,  EN, EN, EN, EN,   QN,  EN, EN, EN, EN,   QN,  EN, EN, EN, EN,
                       DQN, DQN,    QN,  EN, EN, EN, EN,    DQN, DQN,     QN,  EN, EN, EN, EN,     DQN, DQN,      QN, EN, EN,  EN, EN]

block7DoubleBassPitch  = [BF1, REST, REST,    BF1, REST, REST,    BF1, REST, REST,   BF1, REST, REST,   A1,  A1,
                           BF1, REST, REST,     A1,  A1,       BF1, REST, REST,   A1,  A1,      G1, REST, REST]
block7DoubleBassRhythm = [QN,  EN,   DQN,     QN,  EN,   DQN,     QN,  EN,   DQN,    QN,  EN,   DQN,    DQN, DQN, 
                            QN, EN,   DQN,      DQN, DQN,      QN,  EN,   DQN,    DQN, DQN,     QN, EN,   DQN]

block8Violin1Pitch = [E4,  E4,  E4,  E4,  REST, REST] #chords
block8Violin2Pitch = [CS4, D4,  CS4, D4,  REST, REST]
block8ViolaPitch   = [A3,  BF3, A3,  BF3, E3,   E3]
block8UpperRhythm  = [DHN] * 6 #repetetive

block8CelloPitch  = [A2, REST, A2, REST,     G2, REST, G2, REST,   A2, REST, A2, REST,     G2, REST, G2, REST,    CS3,   D3]
block8CelloRhythm = [QN, EN,   QN, EN,       QN, EN,   QN, EN,     QN, EN,   QN, EN,       QN, EN,   QN, EN,      DHN,   DHN]

block8DoubleBassPitch  = [A1, REST, A1, REST, G1, REST, G1, REST] *3   #repetetive
block8DoubleBassRhythm = [QN, EN,   QN, EN,   QN, EN,   QN, EN]   *3

block9SoliPitch  = [A3, E4, E4, FS4,      G4, FS4, E4, D4,     E4, A3, B3, CS4,      D4,  D4, CS4,       A3, E4, E4, FS4, 
                      G4, G4, FS4, E4,     A4,     B4,  B4, CS5,   D5, CS5, B4, A4,     B4,  B4, CS5,   D5, CS5, B4, A4]
block9SoliRhythm = [QN, EN, QN, EN,       QN, EN,  QN, EN,     QN, EN, QN, EN,       DQN, QN, EN,        QN, EN, QN, EN, 
                      QN, EN, QN,  EN,     DHN,    DQN, QN, EN,    QN, EN,  QN, EN,     DQN, QN, EN,    QN, EN,  QN, EN]

block9ViolaPitch      = [E3,  REST, CS4, REST,   B3, REST, B3, REST,    CS4, REST, A3, REST,     B3,     REST,   B3,      REST,      E3,  REST, CS4, REST,
                           B3,       REST,  B3,      REST,     CS4, REST, CS4, REST,      [D4, G3], REST, [D4, G3], REST,     A3, REST, CS4, REST,
                              [D4, G3], REST, [D4, G3], REST,     A3, REST, CS4, REST]
block9CelloPitch      = [CS3, REST, E3,  REST,   D3, REST, D3, REST,    A2,  REST, E3, REST,    [D3, G2], REST, [D3, G2], REST,      CS3, REST, E3,  REST, 
                           [D3, G2], REST, [D3, G2], REST,     E3,  REST, E3,  REST,      [D3, G2], REST, [D3, G2], REST,     E3, REST, E3,  REST,
                              [D3, G2], REST, [D3, G2], REST,     E3, REST, E3,  REST]
block9DoubleBassPitch = ([A2, REST, A2, REST,    G2, REST, G2, REST] * 5) + [A2, REST, A2, REST] #saves space
block9ChordRhythm     = [QN, EN, QN, EN] * 11 #11 measures of QN EN QN EN

block9Violin1Pitch  = [REST] * 11
block9Violin1Rhythm = [EN * 6] * 11

block10Violin1Pitch  = [B3,   CS4, REST, A3, REST,     B3, REST, REST,]
block10Violin1Rhythm = [DHN,  QN,  EN,   QN, EN,       QN, EN,   DQN]

block10Violin2Pitch = [FS4,       FS4,     D4,   E4, A3, B3, CS4,     D4, D4, CS4, B3]
block10ViolaPitch   = [[D4, G3], [D4, G3], D4,   E4, A3, B3, CS4,     D4, D4, CS4, B3]
block10MidRhythm    = [DQN,       QN,      EN,   QN, EN, QN, EN,      QN, EN, QN, EN]

block10CelloPitch      = [[D3, G2], REST, [D3, G2], REST,      E3, REST, E3, REST,     [D3, G2], REST, [D3, G2], REST]
block10DoubleBassPitch = [G2,       REST,  G2,      REST,      A2, REST, A2, REST,      G2,      REST,  G2,      REST]
block10LowerRhythm     = [QN, EN] * 6

#i give up on lining up chords i am sobbing
block11Violin1Pitch = [CS4, REST, REST, REST,    REST,     CS4, REST, REST, REST,    REST,
                         [CS5, E4], REST, E4,       REST,      D4,      REST, [BF4, D4], REST,     E4,       REST, E4,       REST,       D4,      REST, [BF4, D4], REST]
block11Violin2Pitch = [E4,  REST, A3,   REST,    REST,     E4,  REST, A3,   REST,    REST,
                         [A5, A4],  REST, [E5, A4], REST,      G4,      REST, BF5,       REST,    [A5, A4],  REST, [E5, A4], REST,       G4,       REST,  BF5,     REST]
block11ViolaPitch   = [E4,  REST, A3,   REST,    E3,       E4,  REST, A3,   REST,    E3,
                         [CS4, E3], REST, CS4,   REST,     [D4, G3], REST, [D4, G3], REST,   [CS4, E3], REST,  CS4, REST,                 [D4, G3], REST, [D4, G3], REST]
block11UpperRhythm  = [QN,  EN,   QN,   EN,      DHN,      QN,  EN,   QN,   EN,      DHN,     
                          QN,       EN,   QN,    EN,        QN,      EN,   QN,        EN,      QN,       EN,   QN, EN,                    QN,      EN,    QN,     EN]

block11CelloPitch      = [A3, REST, C3, REST,   [D3, G2], REST, [D3, G2], REST,      A3, REST, G3, REST,     [D3, G2], REST, [D3, G2], REST,
                            A2, REST, A3, REST,    BF3, REST, G2, REST,           A2, REST, A3, REST,    BF3, REST, G2, REST]
block11DoubleBassPitch = [A2, REST, A2, REST,    G2, REST, G2, REST,       A2, REST, A2, REST,       G2, REST, G2, REST,
                            A1, REST, A2, REST,    BF2, REST, G1, REST,           A1, REST, A2, REST,    BF2, REST, G1, REST]
block11LowerRhythm     = [QN, EN, QN, EN] * 8

block12SoliPitch  = [A4, E5, E5, FS5,  G5, FS5, E5, D5,    E5, A4, B4, CS5,     D5,  D5, CS5,      A4, E5, E5, FS5,
                       G5, G5, FS5, E5,      A5,      [B4, B5], [B4, B5], [CS4, CS5],   [D4, D5], [CS5, CS6], [B4, B5], [A4, A5],  [B4, B5], [B4, B5], [CS4, CS5],
                           [D4, D5], [CS4, CS5], [B4, B5], [A4, A5],    [FS4, FS5], [FS4, FS5], D5,      E5, A4, B4, CS5,       D5, D5, CS5, B4]
block12SoliRhythm = [QN, EN, QN, EN,   QN, EN, QN, EN,     QN, EN, QN, EN,      DQN, QN, EN,       QN, EN, QN, EN, 
                       QN, EN, QN, EN,       DHN,     DQN,       QN,       EN,          QN,        EN,         QN,       EN,       DQN,       QN,        EN,      
                            QN,        EN,        QN,       EN,          DQN,        QN,        EN,      QN, EN, QN, EN,        QN, EN, QN,  EN]

block12Violin2Pitch    = [[A5, CS5], REST, [E5, A4], REST,     G4, REST, B5, REST,                 [A5, CS5], REST, [E5, A4], REST,      G4,        REST, B5,       REST,
                             [A5, CS5], REST, [E5, A4], REST,     G4,       REST, B5,       REST,      [A5, CS5], REST, [E5, A4], REST,     G4, REST, B5, REST,
                                 [A5, A4], REST, [E5, A4], REST,     G4,       REST, B5,       REST,      A5, REST, [E5, A4], REST,
                                     G4,        REST,     B5,      REST,     [A5, CS5], REST, [E5, A4], REST,     G4,     REST, B5,  REST]
block12ViolaPitch      = [[CS4, E3], REST, CS4,      REST,     [D4, G3], REST, [D4, G3], REST,      [CS4, E3], REST, CS4,     REST,       [D4, G3], REST, [D4, G3], REST,
                             [CS4, E3], REST, CS4,      REST,     [D4, G3], REST, [D4, G3], REST,      [CS4, E3], REST, CS4,  REST,       [D4, G3], REST, [D4, G3], REST,
                                  E4,      REST, CS4,      REST,     [D4, G3], REST, [D4, G3], REST,      E4, REST, CS4,      REST,
                                     [D4, G3], [D4, G3], [D4, G3], D4,       E4,        A3,    B3,      CS4,     [D4, G3], D4,  CS4, B3]

block12CelloPitch      = [A2, REST, A3, REST,      B3, REST, G2, REST] * 7
block12DoubleBassPitch = [A1, REST, A2, REST,      B2, REST, G1, REST] * 7 
block12ChordRhythm     = [QN, EN, QN, EN] * 14

block13Violin1Pitch = [FS5,   CS6,     CS6,     CS6, DS6,      E6,         E6,        DS6,         CS6,       B5,        CS6, FS5,      GS5, AS5]
block13Violin2Pitch = [AS4,   CS5,     CS5,     CS5, DS5,      E5,         E5,        DS5,         CS5,       B4,        CS5, FS4,      GS4, AS4]
block13ViolaPitch   = [FS4,   AS4,     AS4,     AS4, AS4,      [GS4, B3], [GS4, B3], [GS4, B3],   [GS4, B3], [GS4, B3],  AS4, AS4,      GS4, FS4]
block13UpperRhythm  = [DHN,   DHN,     DHN,     DQN, DQN,      DQN,        QN,        EN,          DQN,       DQN,       DQN, DQN,      DQN, DQN]

block13CelloPitch      = [FS2, REST, CS3, REST] * 8
block13DoubleBassPitch = [FS1, REST, CS2, REST] * 8 
block13LowerRhythm     = [QN,  EN,   QN,  EN]   * 8

block14Violin1Pitch = [B5,  B5,  B5]
block14Violin2Pitch = [B4,  B4,  B4]
block14ViolinRhythm = [DHN, DHN, DHN]

block14SoliPitch  = [E4, FS4, G4, G4,      FS4, D4, E4, E4,      FS4, G4, A4, G4, FS4]
block14SoliRhythm = [QN, EN,  QN, EN,      QN,  EN, QN, EN,      QN,  EN, EN, EN, EN]

block14CelloPitch  = [G2, REST, CS3, REST] * 3
block14CelloRhythm = [QN, EN,   QN,  EN]   * 3

block14DoubleBassPitch    = [REST]   * 3
block14DoubleBassRhythm   = [EN * 6] * 3

block15Violin1Pitch = [FS5, CS6,       CS6, DS6,      E6,         E6,        E6,        DS6,       CS6,       FS6,     FS6, REST, REST, REST]
block15Violin2Pitch = [AS4, CS5,       CS5, DS5,      E5,         E5,        E5,        DS5,       CS5,       FS5,     GS5, GS5,  GS5,  AS5]
block15ViolaPitch   = [FS4, AS4,       AS4, AS4,      [GS4, B3], [GS4, B3], [GS4, B3], [GS4, B3], [GS4, B3],  AS4,     AS4, AS4,  AS4,  AS4]
block15UpperRhythm  = [DQN, DQN,       DQN, DQN,      DQN,        QN,        EN,        DQN,       DQN,       DHN,     EN,  QN,   QN,   DQN]

block15CelloPitch      = [FS2, CS3] * 6
block15DoubleBassPitch = [FS1, CS1] * 6
block15LowerRhythm     = [DQN, DQN] * 6

block16Violin1Pitch = [B4, B4, B4]
block16Violin2Pitch = [B5, B5, B5]
             
block17Violin1Pitch = [C5, G5, G5, A5,       BF5, A5, G5, F5,      G5, C5, D5, E5,      F5,  F5, E5]
block17Violin2Pitch = [C4, G4, G4, A4,       BF4, A4, G4, F4,      G4, C4, D4, E4,      F4,  F4, E4]
block17ViolinRhythm = [QN, EN, QN, EN,       QN,  EN, QN, EN,      QN, EN, QN, EN,      DQN, QN, EN]

block17ViolaPitch      = [[B4, E4, G3, C3], REST, [B4, E4, G3, C3], REST,     [F4, BF3],      REST, [F4, BF3],      REST] * 2
block17CelloPitch      = [[C4, E3, G2, C2], REST, [C4, E3, G2, C2], REST,     [BF3, D3, BF2], REST, [BF3, D3, BF2], REST] * 2
block17DoubleBassPitch = [C2,               REST,  C2,              REST,      BF2,           REST,  BF2,           REST] * 2
block17ChordRhythm     = [QN,               EN,    QN,              EN,        QN,            EN,    QN,            EN] * 2

block18Violin1Pitch = [C5, G5, G5, A5,    BF5, BF5, A5, G5,     C6]
block18Violin2Pitch = [C4, G4, G4, A4,    BF4, BF4, A4, G4,     C5]
block18ViolinRhythm = [QN, EN, QN, EN,    QN,  EN,  QN, EN,     DHN]

block18ViolaPitch      = [[B4, E4, G3, C3], REST, [B4, E4, G3, C3], REST,     [F4, BF3],      REST, [F4, BF3],      REST,      
                             [B4, E4, G3, C3], REST, [B4, E4, G3, C3], REST,]
block18CelloPitch      = [[C4, E3, G2, C2], REST, [C4, E3, G2, C2], REST,     [BF3, D3, BF2], REST, [BF3, D3, BF2], REST,
                             [C4, E3, G2, C2], REST, [C4, E3, G2, C2], REST]
block18DoubleBassPitch = [C2,               REST,  C2,              REST,      BF2,           REST,  BF2,           REST,
                              C2,               REST,  C2,             REST]
block18ChordRhythm     = [QN, EN, QN, EN] * 3

block19Violin1Pitch = [D6,  D6, E6,       F6, E6, D6, C6,      D6,  D6, E6,      F6, E6, D6, C6,      [A5, BF4], [A5, BF4], F5]
block19Violin2Pitch = [D5,  D5, E5,       F5, E5, D5, C5,      D5,  D5, E5,      F5, E5, D5, C5,      [A4, D4],  [A4, D4],  F4]
block19ViolinRhythm = [DQN, QN, EN,       QN, EN, QN, EN,      DQN, QN, EN,      QN, EN, QN, EN,       DQN,       QN,       EN]

block19ViolaPitch      = ([[F4, BF3],      REST, [F4, BF3],      REST, [B4, E4, G3, C3], REST, [B4, E4, G3, C3], REST] * 2) + [[F4, BF3],      REST, [F4, BF3],      REST]
block19CelloPitch      = ([[BF3, D3, BF2], REST, [BF3, D3, BF2], REST, [C4, E3, G2, C2], REST, [C4, E3, G2, C2], REST] * 2) + [[BF3, D3, BF2], REST, [BF3, D3, BF2], REST]
block19DoubleBassPitch = ([BF2,            REST, BF2,            REST,  C2,              REST,  C2,              REST] * 2) + [ BF2,           REST,  BF2,           REST]
block19ChordRhythm     = [QN, EN, QN, EN] * 5

block20Violin1Pitch = [G5, C5, D5, E5,       F5, F5, E5, D5,      G5, C5, D5, E5,      F5, F5, E5, D5]
block20Violin2Pitch = [G4, C4, D4, E4,       F4, F4, E4, D4,      G4, C4, D4, E4,      F4, F4, E4, D4]
block20ViolinRhythm = [QN, EN, QN, EN] * 4

block21Violin1Pitch    = [G5,               REST, [A4, E4],  REST,     [BF4, D4], REST, [A5, A4, D4], REST] * 2
block21Violin2Pitch    = [G4,               REST,  G4,       REST,      F4,       REST, [F5, A4],     REST,
                            [A4, E4], REST, G4, REST,      F4, REST, [F5, A4], REST]
block21ViolaPitch      = [[B4, E4, G3, C3], REST, [B4, E4],  REST,     [D4, B4],  REST, [F4, D5],     REST] * 2
block21CelloPitch      = [[C4, E3, G2, C2], REST,  C4,       REST,      D4,       REST,  BF2,         REST,
                             C3,      REST, C4, REST,      D4, REST,  BF2,     REST]
block21DoubleBassPitch = [C2,               REST,  C3,       REST,      D3,       REST,  BF1,         REST] * 2
block21ChordRhythm     = [QN, EN,    QN,      EN,       QN,        EN,    QN,          EN]   * 2

block22Violin1Pitch    = [G5,               REST, [A4, E4], REST,       [BF4, D4], REST, [A5, A4, D4], REST,     REST, [A5, A4, D4], REST,
                            REST, [A5, A4, D4], REST,  [A5, A4, D4], REST, [A5, A4, D4], REST]
block22Violin2Pitch    = [[C5, E4],         REST,  G4,      REST,        F4,       REST, [F5, A4],     REST,     REST, [F5, A4, D4], REST,
                            REST, [F5, A4, D4], REST,  [F5, A4, D4], REST, [F5, A4, D4], REST]
block22ViolaPitch      = [[B4, E4, G3, C3], REST, [B4, E4], REST,      [D4, BF4], REST, [F4, D5],     REST,     REST, [F4, D5],     REST,
                            REST, [F4, D5],     REST,  [F4, D5],     REST, [F4, D5],     REST]
block22CelloPitch      = [C3,               REST, C4,       REST,        D4,       REST,  BF3,         REST,     REST,  BF3,         REST, 
                            REST,  BF3,         REST,   BF3,         REST,  BF3,         REST]
block22DoubleBassPitch = [C2,               REST, C3,       REST,        D3,       REST,  BF2,         REST,     REST,  BF2,         REST, 
                            REST,  BF2,         REST,   BF2,         REST,  BF2,         REST]
block22ChordRhythm     = [QN,               EN,   QN,        EN,         QN,       EN,    QN,          EN,        DQN,  QN,          EN, 
                            DQN,  QN,        EN,      QN,           EN,    QN,          EN]

block23Violin1Pitch    = [REST, [A5, A4, D4], REST, REST, REST,  C4,         C4,      [E5, C6],         REST]
block23Violin2Pitch    = [REST, [F5, A4, D4], REST, REST, REST,  C4,         C4,      [E5, C5, G4],     REST]
block23ViolaPitch      = [REST, [F4, D5],     REST, REST, REST, [C4, C3],   [C4, C3], [B4, E4, G3, C3], REST]
block23CelloPitch      = [REST,  BF3,         REST, REST, REST, [C3, C2],   [C3, C2], [C4, E3, G2, C2], REST]
block23DoubleBassPitch = [REST,  BF2,         REST, REST, REST,  C1,         C1,       C2,              REST]
block23ChordRhythm     = [DQN,  QN,           EN,   DHN,  DHN,   DWN,        DQN,      QN,              EN]

#assigning musical phrases to parts
      #block1, measures 1-8
violinOnePhrase.addNoteList(melodyPitches, melodyRhythm)
violinTwoPhrase.addNoteList(melodyPitches, melodyRhythm)
violaPhrase.addNoteList(melodyPitches, melodyRhythm)
celloPhrase.addNoteList(melodyPitches, melodyRhythm)
doubleBassPhrase.addNoteList(bassLineRest, bassBlock1RestDur)
      #block2 measures 9-12
violinOnePhrase.addNoteList(block2UnisonPitch, block2UnisonRhythm)
violinTwoPhrase.addNoteList(block2UnisonPitch, block2UnisonRhythm)
violaPhrase.addNoteList(block2UnisonPitch, block2UnisonRhythm)
celloPhrase.addNoteList(block2UnisonPitch, block2UnisonRhythm)
doubleBassPhrase.addNoteList(bassLineRest, bassBlock2RestDur)
      #measures 13-20
violinOnePhrase.addNoteList(melodyPitches, melodyRhythm)
violinTwoPhrase.addNoteList(block2Violin2Pitch, block2UnisonRhythm2)
violaPhrase.addNoteList(block2ViolaPitch, block2UnisonRhythm2)
celloPhrase.addNoteList(block2CelloPitch, block2UnisonRhythm2)
doubleBassPhrase.addNoteList(bassLineRest, bassBlock1RestDur)
      #block 3 measures 21-24
violinOnePhrase.addNoteList(block3Violin1Pitch, block3Violin1Rhythm)
violinTwoPhrase.addNoteList(block3Violin2Pitch, block3UnisonRhythm)
violaPhrase.addNoteList(block3ViolaPitch, block3UnisonRhythm)
celloPhrase.addNoteList(block3CelloPitch, block3CelloRhythm)
doubleBassPhrase.addNoteList(block3BassRest, block3BassRestDur)
      #block 4 measures 25-32
violinOnePhrase.addNoteList(melodyUpOnePitches, melodyRhythm)
violinTwoPhrase.addNoteList(block4Violin2Pitch, block4ChordRhythm)
violaPhrase.addNoteList(block4ViolaPitch, block4ChordRhythm)
celloPhrase.addNoteList(block4CelloPitch, block4ChordRhythm)
doubleBassPhrase.addNoteList(block4DoubleBassPitch, block4ChordRhythm)
      #block 5 measures 33-39
violinOnePhrase.addNoteList(block5Violin1Pitch, block5UpperRhythm)
violinTwoPhrase.addNoteList(block5Violin2Pitch, block5UpperRhythm)
violaPhrase.addNoteList(block5ViolaPitch, block5UpperRhythm)
celloPhrase.addNoteList(block5CelloPitch, block5LowerRhythm)
doubleBassPhrase.addNoteList(block5DoubleBassPitch, block5LowerRhythm)
      #block 6 measures 40-43
violinOnePhrase.addNoteList(block6Violin1Pitch, block6UpperRhythm)
violinTwoPhrase.addNoteList(block6Violin2Pitch, block6LowerRhythm)
violaPhrase.addNoteList(block6ViolaPitch, block6UpperRhythm)
celloPhrase.addNoteList(block6CelloPitch, block6LowerRhythm)
doubleBassPhrase.addNoteList(block6DoubleBassPitch, block6DoubleBassRhythm)
      #block 7 measures 44-53
violinOnePhrase.addNoteList(block7Violin1Pitch, block7ViolinRhythm)
violinTwoPhrase.addNoteList(block7Violin2Pitch, block7ViolinRhythm)
violaPhrase.addNoteList(block7ViolaPitch, block7LowerRhythm)
celloPhrase.addNoteList(block7CelloPitch, block7LowerRhythm)
doubleBassPhrase.addNoteList(block7DoubleBassPitch, block7DoubleBassRhythm)
      #block 8 measures 54-59
violinOnePhrase.addNoteList(block8Violin1Pitch, block8UpperRhythm)
violinTwoPhrase.addNoteList(block8Violin2Pitch, block8UpperRhythm)
violaPhrase.addNoteList(block8ViolaPitch, block8UpperRhythm)
celloPhrase.addNoteList(block8CelloPitch, block8CelloRhythm)
doubleBassPhrase.addNoteList(block8DoubleBassPitch, block8DoubleBassRhythm)
      #block 9 measures 60 - 71
violinOnePhrase.addNoteList(block9Violin1Pitch, block9Violin1Rhythm)
violinTwoPhrase.addNoteList(block9SoliPitch, block9SoliRhythm)
violaPhrase.addNoteList(block9ViolaPitch, block9ChordRhythm)
celloPhrase.addNoteList(block9CelloPitch, block9ChordRhythm)
doubleBassPhrase.addNoteList(block9DoubleBassPitch, block9ChordRhythm)
      #block 10 measures 72-74
violinOnePhrase.addNoteList(block10Violin1Pitch, block10Violin1Rhythm)
violinTwoPhrase.addNoteList(block10Violin2Pitch, block10MidRhythm)
violaPhrase.addNoteList(block10ViolaPitch, block10MidRhythm)
celloPhrase.addNoteList(block10CelloPitch, block10LowerRhythm)
doubleBassPhrase.addNoteList(block10DoubleBassPitch, block10LowerRhythm)
      #block 11 measures 75-83
violinOnePhrase.addNoteList(block11Violin1Pitch, block11UpperRhythm)
violinTwoPhrase.addNoteList(block11Violin2Pitch, block11UpperRhythm)
violaPhrase.addNoteList(block11ViolaPitch, block11UpperRhythm)
celloPhrase.addNoteList(block11CelloPitch, block11LowerRhythm)
doubleBassPhrase.addNoteList(block11DoubleBassPitch, block11LowerRhythm)
      #block 12 measures 84-98
violinOnePhrase.addNoteList(block12SoliPitch, block12SoliRhythm)
violinTwoPhrase.addNoteList(block12Violin2Pitch, block12ChordRhythm)
violaPhrase.addNoteList(block12ViolaPitch, block12ChordRhythm)
celloPhrase.addNoteList(block12CelloPitch, block12ChordRhythm)
doubleBassPhrase.addNoteList(block12DoubleBassPitch, block12ChordRhythm)
      #block 13 measures 99-107
violinOnePhrase.addNoteList(block13Violin1Pitch, block13UpperRhythm)
violinTwoPhrase.addNoteList(block13Violin2Pitch, block13UpperRhythm)
violaPhrase.addNoteList(block13ViolaPitch, block13UpperRhythm)
celloPhrase.addNoteList(block13CelloPitch, block13LowerRhythm)
doubleBassPhrase.addNoteList(block13DoubleBassPitch, block13LowerRhythm)
      #block 14 measures 108-111
violinOnePhrase.addNoteList(block14Violin1Pitch, block14ViolinRhythm)
violinTwoPhrase.addNoteList(block14Violin2Pitch, block14ViolinRhythm)
violaPhrase.addNoteList(block14SoliPitch, block14SoliRhythm)
celloPhrase.addNoteList(block14CelloPitch, block14CelloRhythm)
doubleBassPhrase.addNoteList(block14DoubleBassPitch, block14DoubleBassRhythm)
      #block 15 measures 112-118
violinOnePhrase.addNoteList(block15Violin1Pitch, block15UpperRhythm)
violinTwoPhrase.addNoteList(block15Violin2Pitch, block15UpperRhythm)
violaPhrase.addNoteList(block15ViolaPitch, block15UpperRhythm)
celloPhrase.addNoteList(block15CelloPitch, block15LowerRhythm)
doubleBassPhrase.addNoteList(block15DoubleBassPitch, block15LowerRhythm)
      #block 16 measures 119-121
violinOnePhrase.addNoteList(block16Violin1Pitch, block14ViolinRhythm)         #same rhythm
violinTwoPhrase.addNoteList(block16Violin2Pitch, block14ViolinRhythm)         #different chord 
violaPhrase.addNoteList(block14SoliPitch, block14SoliRhythm)                  #viola soli repeats
celloPhrase.addNoteList(block14CelloPitch, block14CelloRhythm)                #same cello part
doubleBassPhrase.addNoteList(block14DoubleBassPitch, block14DoubleBassRhythm) #same number of rests 
      #grand pause
celloPhrase.addNote(REST, QN)
doubleBassPhrase.addNote(REST, QN)
      # block 17, omits middle of piece, starts from BLOCK 9, page 9
violinOnePhrase.addNoteList(block17Violin1Pitch, block17ViolinRhythm)
violinTwoPhrase.addNoteList(block17Violin2Pitch, block17ViolinRhythm)
violaPhrase.addNoteList(block17ViolaPitch, block17ChordRhythm)
celloPhrase.addNoteList(block17CelloPitch, block17ChordRhythm)
doubleBassPhrase.addNoteList(block17DoubleBassPitch, block17ChordRhythm)
      # block 18
violinOnePhrase.addNoteList(block18Violin1Pitch, block18ViolinRhythm)
violinTwoPhrase.addNoteList(block18Violin2Pitch, block18ViolinRhythm)
violaPhrase.addNoteList(block18ViolaPitch, block18ChordRhythm)
celloPhrase.addNoteList(block18CelloPitch, block18ChordRhythm)
doubleBassPhrase.addNoteList(block18DoubleBassPitch, block18ChordRhythm)
      # block 19
violinOnePhrase.addNoteList(block19Violin1Pitch, block19ViolinRhythm)
violinTwoPhrase.addNoteList(block19Violin2Pitch, block19ViolinRhythm)
violaPhrase.addNoteList(block19ViolaPitch, block19ChordRhythm)
celloPhrase.addNoteList(block19CelloPitch, block19ChordRhythm)
doubleBassPhrase.addNoteList(block19DoubleBassPitch, block19ChordRhythm)
      # block 20
violinOnePhrase.addNoteList(block20Violin1Pitch, block20ViolinRhythm)
violinTwoPhrase.addNoteList(block20Violin2Pitch, block20ViolinRhythm)
violaPhrase.addNoteList(block17ViolaPitch, block17ChordRhythm)             #identical rhythm
celloPhrase.addNoteList(block17CelloPitch, block17ChordRhythm)             #and notes
doubleBassPhrase.addNoteList(block17DoubleBassPitch, block17ChordRhythm)  
      #block 21
violinOnePhrase.addNoteList(block21Violin1Pitch, block21ChordRhythm)
violinTwoPhrase.addNoteList(block21Violin2Pitch, block21ChordRhythm)
violaPhrase.addNoteList(block21ViolaPitch, block21ChordRhythm)
celloPhrase.addNoteList(block21CelloPitch, block21ChordRhythm)
doubleBassPhrase.addNoteList(block21DoubleBassPitch, block21ChordRhythm)
      #block 22
violinOnePhrase.addNoteList(block22Violin1Pitch, block22ChordRhythm)
violinTwoPhrase.addNoteList(block22Violin2Pitch, block22ChordRhythm)
violaPhrase.addNoteList(block22ViolaPitch, block22ChordRhythm)
celloPhrase.addNoteList(block22CelloPitch, block22ChordRhythm)
doubleBassPhrase.addNoteList(block22DoubleBassPitch, block22ChordRhythm) 
      #block23 
violinOnePhrase.addNoteList(block23Violin1Pitch, block23ChordRhythm)
violinTwoPhrase.addNoteList(block23Violin2Pitch, block23ChordRhythm)
violaPhrase.addNoteList(block23ViolaPitch, block23ChordRhythm)
celloPhrase.addNoteList(block23CelloPitch, block23ChordRhythm)
doubleBassPhrase.addNoteList(block23DoubleBassPitch, block23ChordRhythm)                                 
#assigning phrases to parts
violinOnePart.addPhrase(violinOnePhrase)
violinTwoPart.addPhrase(violinTwoPhrase)
violaPart.addPhrase(violaPhrase)
celloPart.addPhrase(celloPhrase)
doubleBassPart.addPhrase(doubleBassPhrase)

#assigning parts to score

stPaulJigScore.addPart(violinOnePart)
stPaulJigScore.addPart(violinTwoPart)
stPaulJigScore.addPart(violaPart)
stPaulJigScore.addPart(celloPart)
stPaulJigScore.addPart(doubleBassPart)

#play music

Write.midi(stPaulJigScore, "paul.mid")
Play.midi(stPaulJigScore)
