# [eKYC] Verify Daily/Monthly limit when next month
Tags: ws1, ws1_account_limit, account_limit_37

## Precondition - Create schedule tag > Product > Customer > Account > Inbound balance
* [API][SchedulerTag] Create Scheduler Tag with pause_time "2023-10-31T01:20:00Z"
* [API][Product] Create product
* [API][Customer] Create customer
* [API][CASA] Create CASA account - opening at "2023-10-31T01:20:00Z" with product version id "current_product_version_id"
* [API][PostingInstruction] Inbound Hard Settlement at time stamp "2023-10-31T01:25:00Z" with data - amount "1000000000" - account id "current_account_id" - transaction code "VIKKI_TO_NAPAS,E_BANKING,CASA"

## Get balance and info > Transfer > Shift time > Verify daily/monthly limit
* [API][PostingInstruction] Get balance and info of "current_account_id" at pause time "2023-10-31T01:27:00Z", then Outbound Hard Settlement at time stamp "2023-10-31T02:30:00Z" with data - amount "30000000" - account id "current_account_id" - transaction code "VIRTUAL_CARD_CARD_NOT_PRESENT,CARD,CASA"
* [API][PostingInstruction] Get balance and info of "current_account_id" at pause time "2023-10-31T02:30:00Z", then transfer at time stamp "2023-10-31T02:35:00Z" with data - amount "20000000" - from account id "current_account_id" - to account id "default_account_id" - transaction code "VIKKI_TO_VIKKI,INTERNAL_TRANSFER,E_BANKING,CASA"
* [API][SchedulerTag] Update Scheduler Tag "current_scheduler_tag_id" with pause_time "2023-11-01T02:35:00Z"
* [API][Common] Sleep "30" seconds
* [API][CASA] Verify account "EKYC" - daily limit of CASA account with id "current_account_id" at pause time "2023-11-01T02:35:00Z" should be full limit
* [API][CASA] Verify account "EKYC" - monthly limit of CASA account with id "current_account_id" at pause time "2023-11-01T02:35:00Z" should be full limit

## Get balance and info > Transfer VIRTUAL_CARD_CARD_NOT_PRESENT,CARD,CASA > Verify posting and account limit
* [API][PostingInstruction] Get balance and info of "current_account_id" at pause time "2023-11-01T02:35:00Z", then Outbound Hard Settlement at time stamp "2023-11-01T02:40:00Z" with data - amount "50000000" - account id "current_account_id" - transaction code "VIRTUAL_CARD_CARD_NOT_PRESENT,CARD,CASA"
* [API][SchedulerTag] Update Scheduler Tag "current_scheduler_tag_id" with pause_time "2023-11-01T02:40:00Z"
* [API][Common] Sleep "10" seconds
* [API][PostingInstruction] Verify status of posting id "current_posting_id" should be "POSTING_INSTRUCTION_BATCH_STATUS_ACCEPTED"
* [API][PostingInstruction] Verify Instruction Detail and Transaction code of posting id "current_posting_id" should match with "VIRTUAL_CARD_CARD_NOT_PRESENT,CARD,CASA"
* [API][Balances][Verify] Default balance of "current_account_id" should be "calculated_amount" after making transaction - "success"
* [API][Common] Sleep "2" seconds
* [API][CASA] Verify account "EKYC" - daily limit of CASA account with id "current_account_id" at pause time "2023-11-01T02:40:00Z" should be correct after making transaction - "fail", "fail", "fail", "fail", "success", "fail", "fail", "success", "success"
* [API][CASA] Verify account "EKYC" - monthly limit of CASA account with id "current_account_id" at pause time "2023-11-01T02:40:00Z" should be correct after making transaction - "fail", "success", "success"


