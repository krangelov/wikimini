concrete NamesSpa of Names = CatSpa ** open Prelude, ResSpa, CommonRomance in {

lincat LN = {s : Str;
             p  : Str;
             art : Bool;
             g : Gender;
             num : Number;
             } ;


lin PlainLN n = heavyNP {
      s = \\c => n.s; 
      a = {g = n.g ; n = n.num ; p = P3}
      } ;


lin UseLN n = heavyNP {
      s = \\c => case n.art of {
        True => case n.g of {
          Fem => case n.num of {
            Sg => "la" ++ n.s;
            Pl => "las" ++ n.s} ;
          Masc => case n.num of {
            Sg => "el" ++ n.s;
            Pl => "los" ++ n.s
            }
            } ;
        False => n.s
        } ;
      a = {g = n.g ; n = n.num ; p = P3}
      } ;


lin InLN n = {
      s = n.p ++ case n.art of {
        True => case n.g of {
          Fem => case n.num of {
            Sg => "la" ++ n.s;
            Pl => "las" ++ n.s} ;
          Masc => case n.num of {
            Sg => "el" ++ n.s;
            Pl => "los" ++ n.s
             }
            } ;
        False => n.s
        } ;
  } ;


lin AdjLN ap n = n ** {
      s = preOrPost ap.isPre (ap.s ! AF n.g n.num) n.s ;
    } ;


oper
  mkLN = overload {
    mkLN : Str -> Gender -> LN = \s,g ->
      lin LN {s = s ;
              p = "en" ;
              art = False ;
              g = g ;
              num = Sg} ;

    mkLN : Str -> Gender -> Number -> LN = \s,g,num ->
      lin LN {s = s ;
              p = "en" ;
              art = False ;
              g = g ;
              num = num} ;
  } ;


  defLN : LN -> LN = \n -> n ** {art = True} ;

}