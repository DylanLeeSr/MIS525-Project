#Project lists
materialCostList = []
laborCostList = []
overheadCostList = []
projectBenefitList = []
projectCounter = 0

#Introduction
print('Project Analysis Program')
print('For MIS525')
print('January 2024 Session')
print('By Dylan Lee Sr.')

#Loop for multiple uses and initial data input to lists with input validation for positive numbers and floats
continueAnalysis = 'Y'
while continueAnalysis == 'Y':
    while True:
        try:
            materialCost = (float(input('Enter Material Cost: ')))
            if materialCost > 0:
                materialCostList.append(materialCost)
                break
            else:
                print("Please use positive numbers.")
        except ValueError:
            print("Invalid input. Please enter a valid float.")
    
    while True:
        try:
            laborCost = (float(input('Enter Labor Cost: ')))
            if laborCost > 0:
                laborCostList.append(laborCost)
                break
            else:
                print("Please use positive numbers.")
        except ValueError:
            print("Invalid input. Please enter a valid float.")
        
    while True:
        try:
            overheadCost = (float(input('Enter Overhead Cost: ')))
            if overheadCost > 0:
                overheadCostList.append(overheadCost)
                break
            else:
                print("Please use positive numbers.")
        except ValueError:
            print("Invalid input. Please enter a valid float.")
    
    while True:
        try:
            projectBenefit = (float(input('Enter Projected Benefit: ')))
            if projectBenefit > 0:
                projectBenefitList.append(projectBenefit)
                break
            else:
                print("Please use positive numbers.")
        except ValueError:
            print("Invalid input. Please enter a valid float.")

    continueAnalysis = input('Would you like to enter another project? (Y/N): ')

#Loop for running calculations on each idex in each list and printing the information with recommendations based on profit
for dataItem in materialCostList:
    totalProjectCost = materialCostList[projectCounter] + (laborCostList[projectCounter] + overheadCostList[projectCounter])
    projectProfit = projectBenefitList[projectCounter] - totalProjectCost
    projectProfitPercent = (projectProfit / totalProjectCost) * 100
    print('========================================')
    print(f'--- Summary Report for Project --- {projectCounter + 1}')
    print('Prepared by: Dylan Lee Sr.')
    print(f'Material Cost: {materialCostList[projectCounter]:.2f}')
    print(f'Labor Cost: {laborCostList[projectCounter]:.2f}')
    print(f'Overhead Cost: {overheadCostList[projectCounter]:.2f}')
    print(f'Total Cost: {totalProjectCost:.2f}')
    print(f'Cost Savings or Revenue Increase: {projectBenefitList[projectCounter]:.2f}')
    print(f'Project Profit: {projectProfit:.2f}')
    print(f'Project Return: {projectProfitPercent:.2f}%')

    #Decisions statements for accepting or rejecting the project based on calcuation outputs.
    if projectProfitPercent < 0:
        print("Analysis: Project not recommended for approval based on low profit percentage.")
    elif projectProfitPercent == 0:
        print("Analysis: Neutral based on balanced profit percentage.")
    elif projectProfitPercent <= 5:
        print("Analysis: Recommended for approval based on positive profit percentage.")
    else:
        print("Analysis: Project highly recommended based on exceptional profit percentage.")
    
    #Move to next index in list
    projectCounter += 1
