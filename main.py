#definitions
import garden
import openai_class

#functions

#main
if __name__ == '__main__':
    x=int(input('x demention: '))
    y=int(input('y demention: '))

    g=garden.garden("ogrod")
    garden_array = g.create_field(x,y)
    g.show_garden()

    goods = []
    bads = []
    for xx in range(x-1):
        for yy in range(y):
            question = "can i plan " + str(g.garden[yy][xx]) + " next to " + str(g.garden[yy][xx+1]) + "?"
            response = openai_class.oai.question(question)
            if(str.__contains__(str(response).lower(),'yes')):
                goods.append("can i plan " + str(g.garden[yy][xx]) + " next to " + str(g.garden[yy][xx+1]) + "?" + response)
            else:
                bads.append("can i plan " + str(g.garden[yy][xx]) + " next to " + str(g.garden[yy][xx+1]) + "?" + response)

    for xx in range(x):
        for yy in range(y-1):
            question = "can i plan " + str(g.garden[yy][xx]) + " next to " + str(g.garden[yy+1][xx]) + "?"
            response = openai_class.oai.question(question)
            if (str.__contains__(str(response).lower(), 'yes')):
                goods.append("can i plan " + str(g.garden[yy][xx]) + " next to " + str(g.garden[yy+1][xx]) + "?" + response)
            else:
                bads.append("can i plan " + str(g.garden[yy][xx]) + " next to " + str(g.garden[yy+1][xx]) + "?" + response)

    print("goods:")
    for x in range(len(goods)):
        print(goods[x])

    print("bads:")
    for x in range(len(bads)):
        print(bads[x])
    print(response)







