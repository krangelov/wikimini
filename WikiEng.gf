concrete WikiEng of Wiki =
  GrammarEng [
  Phr, Utt, Pol, ListNP, Adv, Comp, VPSlash, Tense, Card, Cl, Voc, AP,
  Num, S, Conj, Det, NP, Temp, Ant, Quant, Dig, CN, Digits, VP, PConj, Pron,
  Prep, A, V2, N, PN, ListS, AdV,
  PhrUtt,
  PhrUttMark,
  NoPConj,
  UttS,
  UseCl,
  TTAnt,
  TPres,
  ASimul,
  PPos,
  PredVP,
  UsePN,
  UseComp,
  CompNP,
  DetCN,
  DetQuant,
  IndefArt,
  NumSg,
  AdvCN,
  AdjCN,
  PositA,
  UseN,
  PrepNP,
  NumCard,
  NumDigits,
  IIDig,
  D_0,
  D_1,
  D_2,
  D_3,
  D_4,
  D_5,
  D_6,
  D_7,
  D_8,
  D_9,
  NoVoc,
  FullStop,
  UsePron,
  it_Pron,
  ComplSlash,
  SlashV2a,
  NumPl,
  ConjNP,
  and_Conj,
  ConsNP,
  AdvNP,
  DefArt,
  ConjS,
  IDig,
  BaseNP,
  BaseS,
  MassNP,
  AdVVP
  ],
  ExtendEng [
  N,
  CompoundN
  ],
  MiniEng **
open
  Prelude in {
lincat Mark = {s : Str} ;

lin PhrUttMark pconj utt voc mark = {s = pconj.s ++ utt.s ++ voc.s ++ SOFT_BIND ++ mark.s} ;
lin FullStop  = {s = "."} ;

}
