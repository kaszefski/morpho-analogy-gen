import os
from siganalogies import dataset_factory, SERIALIZATION

def dataset_maker(DATASET='2016', LANGUAGE='english'):
    if DATASET == '2016':
        MODE = 'train'
    else:
        MODE = 'train-high'

    try:
        os.mkdir('datasets/'+LANGUAGE)
    except:
        pass

    dataset = dataset_factory(
        dataset=DATASET,
        language=LANGUAGE,
        mode=MODE,
        force_rebuild=False,
        serialization=SERIALIZATION)


    with open('datasets/'+LANGUAGE+'/'+LANGUAGE+"_analogies_"+DATASET+".txt", 'w', encoding='utf-8') as f:
        for x, y in dataset.analogies:
            f.write(dataset.raw_data[x][2]+'\t'+dataset.raw_data[x][0]+'\t'+dataset.raw_data[y][2]+'\t'+dataset.raw_data[y][0]+'\n')



