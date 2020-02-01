# Small search engine 

## Steps
1. Collect obesity data from [CDC website](https://www.cdc.gov/obesity/index.html).
2. Extract features from pre-trained [transformer XL](https://huggingface.co/transformers/model_doc/transformerxl.html#transfoxlmodel) model for each articles.
  - average over sequence_len instead of hidden_state 
3. Extract features for the search input 
4. Calculate cosine similarity between article features and search input feature
5. Output the article with the highest similarity. 


## Results 
Test on 10 articles.
```
the shape of the dataset is: (10, 1)
the dataset is:
['index and risk of 22 specific cancers: a population-based cohort study of 5•24 million UK adults. Lancet. 2014 Aug 30;384(9945):755-65. doi: 10.1016/S0140-6736(14)60892-8. Epub 2014 Aug 13.', 'The Obesity Maps depict self-reported obesity prevalence among U.S. adults. This section offers obesity data maps by state and territory, Powerpoint slides and information about the data methodology and previous years.', '8 Freedman, D.S. et al., 2009. Relation of body mass index and skinfold thicknesses to cardiovascular disease risk factors in children: the Bogalusa Heart Study.  Am. J. Clin. Nutr. , 90(1), pp.210–216.', 'c P<0.001 for trend tests with all years’ data included; P values were obtained from log binomial regression models controlled for age, sex, and race/ethnicity.', 'The Physical Activity Learning Session (PALS) Project, a partnership with the Nemours Foundation, is building the capacity of three states to better integrate physical activity (PA) into statewide ECE technical assistance and training networks so that they can equip ECE providers with the knowledge, skills, and resources to engage and lead infants, toddlers, and preschoolers in PA.', 'Genetic changes in human populations occur too slowly to be responsible for the obesity epidemic. Nevertheless, the variation in how people respond to the environment that promotes physical inactivity and intake of high-calorie foods suggests that genes do play a role in the development of obesity.', 'Young adults were half as likely to have obesity as middle-aged adults. Adults aged 18-24 years had the lowest self-reported obesity (18.1%) compared to adults aged 45-54 years who had the highest prevalence (36.9%).', 'Table 1. Prevalence of Overweight or Obesity Among U.S. Children Aged 2–4 Years Enrolled in WIC by Age, Sex, and Race/Ethnicity, 2010-2016', 'CORD: A Supplement to the Journal, Childhood Obesity external icon  is a special issue of research articles of baseline assessments related to the CORD Project.', 'Childhood Obesity Research Demonstration (CORD) Projects  We focus on improving community-clinical collaborations to help prevent and manage childhood obesity in low-income children. We test a model that increases obesity screening and counseling services for eligible children in the selected communities, and refers them to local pediatric weight management programs. These findings help inform our childhood obesity efforts across the nation.']

the input text is: Childhood Obesity

similarity scores of all:

[0.15124276280403137, 0.2569819986820221, 0.22031140327453613, 0.12661898136138916, 0.14201630651950836, 0.1699725240468979, 0.24751237034797668, 0.3248971402645111, 0.279965877532959, 0.4296077489852905]
The highest similar data in the dataset: 
Childhood Obesity Research Demonstration (CORD) Projects  We focus on improving community-clinical collaborations to help prevent and manage childhood obesity in low-income children. We test a model that increases obesity screening and counseling services for eligible children in the selected communities, and refers them to local pediatric weight management programs. These findings help inform our childhood obesity efforts across the nation.
```

Adopted from [Building a Search Engine with BERT and TensorFlow](https://towardsdatascience.com/building-a-search-engine-with-bert-and-tensorflow-c6fdc0186c8a)
