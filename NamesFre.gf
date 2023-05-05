concrete NamesFre of Names = CatFre ** open Prelude, ResFre, CommonRomance, PhonoFre in {

param
  HasArt = NoArt | UseArt | AlwaysArt ;


lincat LN = {s  : Str;
             p  : Compl;
             art : HasArt;
             g : Gender;
             num : Number;
             } ;


lin PlainLN n = heavyNP {
      s = \\c => n.s; 
      a = {g = n.g ; n = n.num ; p = P3}
      } ;


lin UseLN n = heavyNP {
      s = \\c => case n.art of {
        AlwaysArt | UseArt => artDef True n.g n.num c ++ n.s ;
        _      => n.s
        } ;
      a = {g = n.g ; n = n.num ; p = P3}
  } ;


lin InLN n = {
      s = n.p.s ++ case n.art of {
        AlwaysArt => artDef True n.g n.num n.p.c ++ n.s;
        _         => prepCase n.p.c ++ n.s
        } ;
  } ;


lin AdjLN ap n = n ** {
      s = preOrPost ap.isPre (ap.s ! AF n.g n.num) n.s ;
    } ;    


oper
  mkLN = overload {
    mkLN : Str -> Gender -> LN = \s,g ->
      lin LN {s = s ;
              p =  {s=""; c=CPrep P_a; isDir=True} ;
              art = NoArt ;
              g = g ;
              num = Sg} ;

    mkLN : Str -> Gender -> Number -> LN = \s,g,num ->
      lin LN {s = s ;
              p = {s=""; c=CPrep P_a; isDir=True} ;
              art = NoArt ;
              g = g ;
              num = num} ;
  } ;


  defLN : LN -> LN = \n -> n ** {art = AlwaysArt} ;
  useDefLN : LN -> LN = \n -> n ** {art = UseArt} ;
  prepLN : LN -> Compl -> LN = \n,s -> n ** {p = s} ;

}