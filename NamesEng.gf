concrete NamesEng of Names = CatEng ** open Prelude, ResEng in {

lincat LN = {s  : Case => Str;
             p  : Str;   -- preposition "in Scandinavia", "on the Balkans"
             art : Bool; -- plain name "United States" vs "the United States"
             a  : Agr;
            } ;

lin UseLN n = {
      s = \\c => case n.art of {
                   True  => "the" ++ n.s ! npcase2case c ;
                   False => n.s ! npcase2case c
                 } ;
      a = n.a
    } ;

lin PlainLN n = {
      s = \\c => n.s ! npcase2case c ;
      a = n.a
    } ;

lin InLN n = {
      s = n.p ++ case n.art of {
                   True  => "the" ++ n.s ! Nom ;
                   False => n.s ! Nom
                 } ;
    } ;
    
lin AdjLN ap n = n ** {
      s = \\c => preOrPost ap.isPre (ap.s ! n.a) (n.s ! c) ;
    } ;

oper
  mkLN = overload {
    mkLN : Str -> LN = \s ->
      lin LN {s = table {Gen => s + "'s" ; _ => s} ; 
              p = "in" ;
              art = False ;
              a = agrP3 Sg} ;

    mkLN : Str -> Number -> LN = \s,n ->
      lin LN {s = table {Gen => s + "'s" ; _ => s} ;
              p = "in" ;
              art = False ;
              a = agrP3 n} ;
  } ;

  defLN : LN -> LN = \n -> n ** {art = True} ;
  prepLN : LN -> Str -> LN = \n,s -> n ** {p = s} ;

}
