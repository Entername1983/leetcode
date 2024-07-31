## second lowest score
## Bob: 20, Sarah: 40, John: 19

"""Bob --> lowest with 20
Store Bob in lowest names, store lowest score as 20
Sarah --> higher than lowest
Store Sarah as second lowest names, second lowest as 40
John --> lower than lowest
    Lowest --> second lowest
    Second lowest gets reset
## score can be higher than lowest but lower than second lowest
## score can be equal to second lowest
## score can be higher than second lowest --> ignore

"""




if __name__ == '__main__':
    records: list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        
    lowest: dict = {"score": 100, "names": []}
    second_l: dict = {"score": 100, "names": []}

    for record in records:
        
        if record[1] < lowest['score']: ## score can be lower than lowest
             ## if we find a lower score need to check if the lowest score is lower than second lowest
            second_l['score'] = lowest['score']
            second_l['names'] = lowest['names']
            lowest['score'] = record[1]
            lowest['names'] = [record[0]]
            
        elif record[1] == lowest['score']: ## score can be equal to lowest
            lowest['names'].append(record[0]) ## if there is a matching lowest score then we just add the current name to the list
            
        elif lowest['score'] < record[1] < second_l['score']:
            second_l['score'] = record[1]
            second_l['names']= [record[0]]
        
        elif record[1] == second_l['score']:
            second_l['names'].append(record[0])
            
    second_l['names'].sort()
    for name in second_l['names']:
        print(name)
            