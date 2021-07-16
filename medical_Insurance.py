# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(name,age,sex,bmi,num_of_children,smoker):
  estimated_cost=250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  msg=print("The estimated_cost for "+name+" is "+str(estimated_cost)+" dollars.")
  return estimated_cost,msg
  

# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost("Maria",28,0,26.2,3,0)

# Estimate Omar's insurance cost 
omar_insurance_cost = calculate_insurance_cost("Omar",35,1,22.2,0,1)
# Estimate Michael's insurance cost 
mikel_insurance_cost = calculate_insurance_cost("Michael S",27,1,20.5,0,0)

# Estimate Beatrice's insurance cost 
ama_insurance_cost= calculate_insurance_cost("Beatrice",25,0,28.4,1,0)

# difference of insurance cost
def differ_insurance_cost(insure_cost1,insure_cost2):
  total_differences=insure_cost1-insure_cost2
  return print("The difference in insurance cost is "+str(total_differences)+" dollars")

differ_insurance_cost(ama_insurance_cost[0],mikel_insurance_cost[0])
