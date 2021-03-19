# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# from __future__ import unicode_literals

# from django.db import models


# class SpiceirExternalData(models.Model):
#     id = models.AutoField(db_column='ID',primary_key=True)  # Field name made lowercase.
#     account_number = models.CharField(db_column='Account_Number', primary_key=True, max_length=50)  # Field name made lowercase.
#     customer_name = models.CharField(db_column='Customer_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     trans_amt_latest_autopay = models.CharField(db_column='Trans_Amt_Latest_Autopay', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     total_current = models.CharField(db_column='Total_Current', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     account_status = models.CharField(db_column='Account_Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     recurring_charges = models.CharField(db_column='Recurring_Charges', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     credit_limit_amt = models.CharField(db_column='Credit_Limit_Amt', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     used_credit_limit = models.CharField(db_column='Used_Credit_Limit', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     overdue_charges = models.CharField(db_column='Overdue_Charges', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     trans_date_latest_payment = models.CharField(db_column='Trans_Date_Latest_Payment', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     trans_amt_2nd = models.CharField(db_column='Trans_Amt_2nd', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     trans_date_2nd = models.CharField(db_column='Trans_Date_2nd', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     bill_due_date = models.CharField(db_column='Bill_Due_Date', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     outstanding_amt = models.CharField(db_column='Outstanding_Amt', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     subscript_plan = models.CharField(db_column='Subscript_Plan', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     trans_amt_latest_payment = models.CharField(db_column='Trans_Amt_Latest_Payment', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     trans_date_latest_autopay = models.CharField(db_column='Trans_Date_Latest_Autopay', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     autopay_status = models.CharField(db_column='Autopay_Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     datetime_push = models.CharField(db_column='Datetime_Push', max_length=50, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'spiceir_external_data'