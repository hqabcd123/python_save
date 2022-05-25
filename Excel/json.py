import json

def main():
    print('open json')
    dic = {
        'a':100,
        'b':200
        }
    with open('test.json', 'a+') as fp:
        json.dump(dic)



main()
if __name__ == "__main__":
    pass