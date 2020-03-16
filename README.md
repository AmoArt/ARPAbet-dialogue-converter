# ARPAbet-dialogue-converter
Converts dialogue text for Waveglow training to ARPAbet

Requires python 3 (preferably 3.7)



your file needs to be first saved as plain text file and the components written in the formar of "audiofile.wav|Transcript;",  example:

audiofile0001.wav|Hello.;



How to test if your text file require a csutom dictionary file.

Run both scrips normaly, than open the output file in Notepad+++

-howisthis.wav|{HH AW1} {IH0 S} this?;

Open 'Replace' window and activate the 'Search mode' 'Regular Expresion'

than replace all .*?\| with nothing to create this:

-{HH AW1} {IH0 S} this?;

Replace (\{).*?(\}) with nothing:

-this?;

After that switch to 'Search mode Normal' and replace any semicolon, commas, fullstops, question marks and explanation marks from text. 
Than open 'Edit' 'Line Operations' 'Remove Empty Lines'
Lastly open 'Edit' 'Line Operations' 'Sort Lines Lexicograpgycally Asending', remove any duplicates. 

Save them into new text file in dictionaries folder, use the words in other ARPAbet dictionaries to create new pronunciation list. 


PS. Before using the script it would be recomend to convert any special symols such as "…" either into asci friendly format ("...") or just remove them with 'replace' tool as python script may in rare occasion have trouble handling those kind of elements.
