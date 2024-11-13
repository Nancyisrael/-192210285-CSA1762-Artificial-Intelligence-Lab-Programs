person(nancy,date(2003,7,14)).
person(blessy,date(1932,4,23)).
person(gracy,date(2004,5,21)).
dob_for_person(Name,DOB):-person(Name,DOB).
is_person_in_db(Name):-person(Name,_).
