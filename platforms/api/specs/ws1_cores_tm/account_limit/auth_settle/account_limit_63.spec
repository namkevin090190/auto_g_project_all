# [eKYC] Verify user make transaction successfully on different month with Auth = Settle
Tags: ws1, ws1_account_limit, account_limit_63

## VIRTUAL_CARD_CARD_NOT_PRESENT,CARD,CASA - Including INTEREST
* [API][SchedulerTag] Create Scheduler Tag with pause_time "2023-10-31T01:20:00Z"
* [API][Product] Create product
* [API][Customer] Create customer
* [API][CASA] Create CASA account - opening at "2023-10-31T01:20:00Z" with product version id "current_product_version_id"
* [API][PostingInstruction] Inbound Hard Settlement at time stamp "2023-10-31T01:25:00Z" with data - amount "1000000000" - account id "current_account_id" - transaction code "VIKKI_TO_NAPAS,E_BANKING,CASA"
* [API][Product] Get product info of Product version id "current_product_version_id"
* [API][PostingInstruction] Get balance and info of "current_account_id" at pause time "2023-10-31T01:25:00Z", then Authorisation at time stamp "2023-10-31T01:30:00Z" with data - amount "30000000" - account id "current_account_id" - transaction code "VIRTUAL_CARD_CARD_NOT_PRESENT,CARD,CASA"
* [API][SchedulerTag] Update Scheduler Tag "current_scheduler_tag_id" with pause_time "2023-11-01T01:20:00Z"
* [API][Common] Sleep "30" seconds
* [API][CASA] Get CASA account with id "current_account_id" with pause time "2023-11-01T01:20:00Z"
* [API][Common] Sleep "2" seconds
* [API][PostingInstruction] Settlement at time stamp "2023-11-01T01:25:00Z" with data - amount "30000000" - account id "current_account_id" - transaction code "VIRTUAL_CARD_CARD_NOT_PRESENT,CARD,CASA" - client transaction id order "1"
* [API][Common] Sleep "5" seconds
* [API][PostingInstruction] Verify status of posting id "current_posting_id" should be "POSTING_INSTRUCTION_BATCH_STATUS_ACCEPTED"
* [API][PostingInstruction] Verify Instruction Detail and Transaction code of posting id "current_posting_id" should match with "VIRTUAL_CARD_CARD_NOT_PRESENT,CARD,CASA"
* [API][Balances][Verify] Default balance of "current_account_id" should be "calculated_amount" after making settlement with interest - "success" - client transaction id order "1"
* [API][Common] Sleep "2" seconds
* [API][CASA] Verify account "EKYC" - daily limit of CASA account with id "current_account_id" at pause time "2023-11-01T01:25:00Z" should be full limit
* [API][CASA] Verify account "EKYC" - monthly limit of CASA account with id "current_account_id" at pause time "2023-11-01T01:25:00Z" should be full limit