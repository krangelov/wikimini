## Errors
- country names should in many cases be introduced by an definite articles, e.g.
    > Canada é una nazione in Nordamerica -> Il Canada é una nazione in Nordamerica
- `it_Pron` should linearize to "esso" (neutrum), not "lui" (masculine)
- "l'area é X km²" ("the area is X km²") needs a preposition "l'area é _di_ X km²" (or "l'area é _pari a_ X km²")
- missing `CompoundN`
- cardinal points do not require an article:
    > "a l'est" -> "ad est"
- "has borders with" sentences with cardinal points are linearized in the wrong order. For instance:
    > "ha frontiere con Malta a sud, Mar Adriatico ad est ed Algeria" -> "ha frontiere/confina con a sud Malta, ad est (con) Mar Adriatico ed Algeria"

## Disfluencies
- pronoun drops would improve idiomacy, e.g.
    > (esso) ha frontiere con...
- "avere frontiere" ("to have borders with") is not really used. The verb "confinare" is much more common
- `AdjCN (PositA spoken_A) (UseN language_1_N)` linearizes to "lingua parlata", but that makes me think of the concept of oral language rather than that of local language, which I guess is the intended one
- I don't know if it is desirable to have so many language names preceeded by the word "lingua" ("language"), especially in long lists such as
    > l' inglese ed il francese sono le lingue ufficiali ma la _lingua_ oneida , la _lingua_ onondaga , il tuscarora , la _lingua_ chipewyan , la _lingua_ algonchina , la _lingua_ tlingit , il mohawk , la _lingua_ cayuga , la _lingua_ blackfoot , il cree , la _lingua_ haida , il filippino e la lingua tsimshian vengono inoltre parlati .
  Also, there should be a criterion to decide whether to include "lingua" or not
- in sentences like the above one, a much better phrasing would be "le lingue ufficiali sono l'inglese ed il francese, ma _si parlano_[^1] _anche_[^2] la lingua oneida, la lingua ondonga, il tuscarora..." (verbs first)

[^1]: "_si_ passivante" (more common in impersonal phrases thn using the passive form of the verb)
[^2]: most importantly, the adverb "inoltre" is currently misplaced. I would also replace it with "anche" but I don't have a good argument for that