abstract Wiki =
  Grammar [
  Phr, Utt, Pol, ListNP, Adv, Comp, VPSlash, Tense, Card, Cl, Voc, AP,
  Num, S, Conj, Det, NP, Temp, Ant, Quant, Dig, CN, Digits, VP, PConj, Pron,
  Prep, A, V2, N, PN, ListS, 
  PhrUtt,
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
  BaseS,
  BaseNP,
  MassNP
  ],
  Extend [
  N,
  CompoundN
  ],
  Mini
  ** {
flags startcat = Phr ;

cat Mark ;

fun PhrUttMark : PConj -> Utt -> Voc -> Mark -> Phr ;
fun FullStop : Mark ;

}
