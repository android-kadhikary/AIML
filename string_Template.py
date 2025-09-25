from string import Template
setdetails={"a":90, "b":98,"c":99, "d":95}

main_title_for_all_candidate= Template(""" Congratulations dear $name,
 we are proud that you got $yourmarks % marks""")


for key,value in setdetails.items():
    greet=main_title_for_all_candidate.substitute(name=key,yourmarks=value )
    print(greet)


names = ["a", "b" "c", "d"]
marks= [98,97,92,99]
zipped_name_mark=dict(zip(names,marks))
# for name, mark in zipped_name_mark:
for named, markd in zipped_name_mark.items():# dict is an iterator
    greet=main_title_for_all_candidate.substitute(name=named,yourmarks=markd )
    print(greet)    


zipped_name_mark=zip(names,marks)
# for name, mark in zipped_name_mark:
for named, markd in zipped_name_mark:#zipped is an iterator
    greet=main_title_for_all_candidate.substitute(name=named,yourmarks=markd )
    print(greet)  