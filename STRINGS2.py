print "hello"

print "hello" .capitalize()

string1 = "see on näide."
print string1.center( 50 )

"see on näide." .center(30, '-')

"Hello world, hello friends".count("ll",0,5)

"Tere tulemast".encode("utf-16")

'\xff\xfeT\x00e\x00r\x00e\x00 \x00t\x00u\x00l\x00e\x00m\x00a\x00s\x00t\x00'.decode("utf-16")

"Tere Tulemast" .endswith ("st")

"Tere Tulemast" .endswith ("st",1,7)

"Tere\ttulemast".expandtabs()
"Tere\ttulemast".expandtabs(15)

"Tere tulemast, Tere" .find("ere")
"Tere tulemast, Tere" .find("ere", 3,10)
"Tere tulemast, Tere" .find("ere", 3,20)

"kui liita 5 + 3 saame {0}" .format (5+3)

"Tere tulemast, Tere" .index("ere", 3,10)

"Tere tulem2st" .isalnum()
"Tere0tulem2st" .isalnum()
"9/2009".isdigit()
"92009".isdigit()
"Hello world".islower()
"hello world".islower()
"Tere Tulemast" .istitle()
"TERE TULEMAST" .isupper()
" " .join(('1','2','3','4'))
