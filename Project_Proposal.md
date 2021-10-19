
# Classification Project Proposal

## Backstory
Diamond Cut is how well a diamond is cut and polished, including how well-proportioned the stone is, its depth and symmetry. 
Diamond Cut doesn’t refer to the shape of the diamond, such as an Oval or Pear Shape. Cut quality directly impacts the diamond’s beauty and brilliance. 
A well cut diamond is luminous and reflects white and colored light back to your eyes. A poorly cut diamond is dull instead of brilliant. 
GIA diamond cutting grades for Round diamonds range from Excellent to Poor. 
The reality is that 55% of all Round diamonds receive an excellent cut grade from the GIA. About 25-30% of these “excellent” diamonds are not recommended. 
[The Diamond Pro](https://www.diamonds.pro/) claimed that their consultants review thousands of Excellent cut diamonds and find bad specs (depth, table and angles). 


## Question/need:

**What is the framing question of your analysis, or the purpose of the model/system you plan to build?**

The proposed project will help clients to double check the cut grade so they don’t end up paying for an ideal cut diamond that’s only mediocre.


**Who benefits from exploring this question or building this model/system?**

* Diamond Store owners.
* Diamond customers (buyers).


## Data Description:

**What dataset(s) do you plan to use, and how will you obtain the data?**

I will use diamond dataset which is obtained from Kaggle, can be found [here](https://www.kaggle.com/shrutisaxena0617/exploring-diamonds-dataset/data)

**What is an individual sample/unit of analysis in this project? What characteristics/features do you expect to work with?**

The prediction will depend on various features such as the depth, length, width, weight, color, price, clarity.

**If modeling, what will you predict as your target?**

The target variable is the cut grade variable which contains the values (Fair, Good, Very Good, Premium, Ideal).



## Tools:
**How do you intend to meet the tools requirement of the project?**

The following libraries will be used in order to successfully complete the project.
* Numpy and pandas to perfom data manipulations.
* Matplotlib to plot visulalizations
* Sklearn to build various classification models.

**Are you planning in advance to need or use additional tools beyond those required?**

I might use production tools to build a small app that predicts the diamond cut grade.

## MVP Goal:
**What would a minimum viable product (MVP) look like for this project?**

The expected outcome of this project is a prediction of the diamond cut grade. A small app that predicts the cut of the diamond and a presentation.
