from monkeylearn import MonkeyLearn

f = open(r"C:\Users\Bartoszek\Desktop\TaernTradeHistory\procesed20.08.23.txt", "r")

ml = MonkeyLearn('e22c23c2a862fc615f87f4b14afbcade0c7410a6')
model_id = 'ex_UgqX2oDD'
data = ['first text', {'text': 'PanZajączek: kupie egzekutor sprzedam:  30 mięska 1:50k'}, '']
response = ml.extractors.extract(model_id, data=data)
for extraction in response.body[1]['extractions']:
    print(extraction['tag_name'] + ': ' + extraction['parsed_value'])
