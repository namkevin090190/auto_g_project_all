# End-2-end
Tags: ws1, ws1_interest, e2e_interest

## Scenario
* [API][SchedulerTag] Create Scheduler Tag with pause_time "2023-10-26T01:20:00Z"
* [API][Product] Create product
* [API][Customer] Create customer
* [API][CASA] Create CASA account - opening at "2023-10-26T01:20:00Z" with product version id "current_product_version_id"
* [API][PostingInstruction] Inbound Hard Settlement at time stamp "2023-10-26T01:25:00Z" with data - amount "2000000000" - account id "current_account_id" - transaction code "VIKKI_TO_NAPAS,E_BANKING,CASA"
* [API][SchedulerTag] Update Scheduler Tag "current_scheduler_tag_id" with pause_time "2023-10-26T01:27:00Z"
* [API][Common] Sleep "10" seconds

* [API][Product] Get product info of Product version id "current_product_version_id"

* [API][Balances] Get balances of "current_account_id"
* [API][SchedulerTag] Update Scheduler Tag "current_scheduler_tag_id" with pause_time "2023-10-26T14:20:00Z"
* [API][Common] Sleep "30" seconds
* [API][Balances][Verify] Accrual Interest balance of "current_account_id" should be "calculated_amount" at "EOD"
* [API][PostingInstruction] Verify status of "CALCULATE DAILY INTEREST" posting of account id "current_account_id" in time range "2023-10-26T01:59:00Z" - "2023-10-26T16:02:00Z" should be "POSTING_INSTRUCTION_BATCH_STATUS_ACCEPTED"

* [API][Balances] Get balances of "current_account_id"
* [API][SchedulerTag] Update Scheduler Tag "current_scheduler_tag_id" with pause_time "2023-10-27T14:20:00Z"
* [API][Common] Sleep "30" seconds
* [API][Balances][Verify] Accrual Interest balance of "current_account_id" should be "calculated_amount" at "EOD"

* [API][Balances] Get balances of "current_account_id"
* [API][SchedulerTag] Update Scheduler Tag "current_scheduler_tag_id" with pause_time "2023-10-28T14:20:00Z"
* [API][Common] Sleep "30" seconds
* [API][Balances][Verify] Accrual Interest balance of "current_account_id" should be "calculated_amount" at "EOD"

* [API][PostingInstruction] Inbound Hard Settlement at time stamp "2023-10-28T14:25:00Z" with data - amount "70000000" - account id "current_account_id" - transaction code "VIKKI_TO_NAPAS,E_BANKING,CASA"
* [API][SchedulerTag] Update Scheduler Tag "current_scheduler_tag_id" with pause_time "2023-10-28T14:30:00Z"
* [API][Common] Sleep "10" seconds

* [API][Balances] Get balances of "current_account_id"
* [API][SchedulerTag] Update Scheduler Tag "current_scheduler_tag_id" with pause_time "2023-10-29T14:20:00Z"
* [API][Common] Sleep "30" seconds
* [API][Balances][Verify] Accrual Interest balance of "current_account_id" should be "calculated_amount" at "EOD"
* [API][PostingInstruction] Verify status of "CALCULATE DAILY INTEREST" posting of account id "current_account_id" in time range "2023-10-29T01:59:00Z" - "2023-10-29T16:02:00Z" should be "POSTING_INSTRUCTION_BATCH_STATUS_ACCEPTED"

* [API][PostingInstruction] Outbound Hard Settlement at time stamp "2023-10-29T14:25:00Z" with data - amount "50000000" - account id "current_account_id" - transaction code "VIRTUAL_CARD_CARD_NOT_PRESENT,CARD,CASA"
* [API][SchedulerTag] Update Scheduler Tag "current_scheduler_tag_id" with pause_time "2023-10-29T14:30:00Z"
* [API][Common] Sleep "10" seconds

* [API][Balances] Get balances of "current_account_id"
* [API][SchedulerTag] Update Scheduler Tag "current_scheduler_tag_id" with pause_time "2023-10-30T14:20:00Z"
* [API][Common] Sleep "30" seconds
* [API][Balances][Verify] Accrual Interest balance of "current_account_id" should be "calculated_amount" at "EOD"
* [API][Balances][Verify] Default balance of "current_account_id" should be "calculated_amount" with interest at "EOD"
* [API][PostingInstruction] Verify status of "CALCULATE DAILY INTEREST" posting of account id "current_account_id" in time range "2023-10-30T01:59:00Z" - "2023-10-30T16:02:00Z" should be "POSTING_INSTRUCTION_BATCH_STATUS_ACCEPTED"

* [API][Balances] Get balances of "current_account_id"
* [API][SchedulerTag] Update Scheduler Tag "current_scheduler_tag_id" with pause_time "2023-10-31T14:20:00Z"
* [API][Common] Sleep "30" seconds
* [API][Balances][Verify] Accrual Interest balance of "current_account_id" should be "calculated_amount" at "EOM"
* [API][Balances][Verify] Default balance of "current_account_id" should be "calculated_amount" with interest at "EOM"
* [API][PostingInstruction] Verify status of "CALCULATE DAILY INTEREST" posting of account id "current_account_id" in time range "2023-10-31T01:59:00Z" - "2023-10-31T16:02:00Z" should be "POSTING_INSTRUCTION_BATCH_STATUS_ACCEPTED"
* [API][PostingInstruction] Verify status of "REVERT CALCULATED INTEREST LUMP SUM" posting of account id "current_account_id" in time range "2023-10-31T01:59:00Z" - "2023-10-31T16:02:00Z" should be "POSTING_INSTRUCTION_BATCH_STATUS_ACCEPTED"
* [API][PostingInstruction] Verify status of "PAY INTEREST TO CUSTOMER" posting of account id "current_account_id" in time range "2023-10-31T01:59:00Z" - "2023-10-31T16:02:00Z" should be "POSTING_INSTRUCTION_BATCH_STATUS_ACCEPTED"