
print("Project Analysis Program")
print("For MIS525")
print("January 2024 Session")
print("By Dylan Lee Sr.")

materialCostString = input("Enter Material Cost:")
materialCost = float(materialCostString)

laborCostString = input("Enter Labor Cost:")
laborCost = float(laborCostString)

overheadCostString = input("Enter Overhead Cost:")
overheadCost = float(overheadCostString)

projectBenifitString = input("Enter Project Benefit:")
projectBenefit = float(projectBenifitString)

totalProjectCost = materialCost + (laborCost + overheadCost)

projectProfit = projectBenefit - totalProjectCost

projectProfitPercent = (projectProfit / totalProjectCost) * 100

print("---Project Summary Report---")
print("Prepared by: Dylan Lee Sr.")
print(f"Material Cost: {materialCost}")
print(f"Labor Cost: {laborCost}")
print(f"Overhead Cost: {overheadCost}")
print(f"Total Cost: {totalProjectCost}")
print(f"Cost Savings or Revenue Increase: {projectBenefit}")
print(f"Project Profit: {projectProfit}")
print(f"Project Return: {projectProfitPercent:.2f}%")

if projectProfitPercent < 0:
    print("Analysis: Project not recommended for approval based on low profit percentage.")
elif projectProfitPercent == 0:
    print("Analysis: Neutral based on balanced profit percentage.")
elif projectProfitPercent <= 5:
    print("Analysis: Recommended for approval based on positive profit percentage.")
else:
    print("Analysis: Project highly recommended based on exceptional profit percentage.")