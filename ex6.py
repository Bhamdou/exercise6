text = """One morning, when Gregor Samsa woke from troubled dreams, 
he found himself transformed in his bed into a horrible vermin.
He lay on his armour-like back, and if he lifted his head a 
little he could see his brown belly, slightly domed and divided by 
arches into stiff sections. The bedding was hardly able to cover 
it and seemed ready to slide off any moment. His many legs, pitifully 
thin compared with the size of the rest of him, waved about helplessly 
as he looked.""" 
hello = "hello"
mark = ""
for x in hello:
    while x in text:
        x = mark + x
        mark = x
        break
    print(mark.capitalize(),(text.split())[3])