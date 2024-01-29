#Introduction
print("Project Analysis Program")
print("For MIS525")
print("January 2024 Session")
print("By Dylan Lee Sr.")

#Loop for continued use for other project calculations.
continueAnalysis = "Y"
while continueAnalysis == "Y":

#Variables
    materialCostString = input("Enter Material Cost:")
    materialCost = float(materialCostString)

    laborCostString = input("Enter Labor Cost:")
    laborCost = float(laborCostString)

    overheadCostString = input("Enter Overhead Cost:")
    overheadCost = float(overheadCostString)

    projectBenifitString = input("Enter Project Benefit:")
    projectBenefit = float(projectBenifitString)



    #Calculations for the total cost of the project, profit, and profit as a percentage.
    totalProjectCost = materialCost + (laborCost + overheadCost)

    projectProfit = projectBenefit - totalProjectCost

    projectProfitPercent = (projectProfit / totalProjectCost) * 100

    #Printing out the results of the calculations.
    print("---Project Summary Report---")
    print("Prepared by: Dylan Lee Sr.")
    print(f"Material Cost: {materialCost}")
    print(f"Labor Cost: {laborCost}")
    print(f"Overhead Cost: {overheadCost}")
    print(f"Total Cost: {totalProjectCost}")
    print(f"Cost Savings or Revenue Increase: {projectBenefit}")
    print(f"Project Profit: {projectProfit}")
    print(f"Project Return: {projectProfitPercent:.2f}%")

    #Decisions statements for accepting or rejecting the project based on calcuation outputs.
    if projectProfitPercent < 0:
        print("Analysis: Project not recommended for approval based on low profit percentage.")
    elif projectProfitPercent == 0:
        print("Analysis: Neutral based on balanced profit percentage.")
    elif projectProfitPercent <= 5:
        print("Analysis: Recommended for approval based on positive profit percentage.")
    else:
        print("Analysis: Project highly recommended based on exceptional profit percentage.")

    continueAnalysis = input("Would you like to analyze another project? (Y/N):")