# Verify Daily/Monthly limit update correctly when upgrade customer from eKYC to FullKYC
Tags: ws1, ws1_account_limit, account_limit_39

## Create Customer > Account > Inbound balance > Get balance and info > Make ebanking trx to reduce ebanking limit > Grant VKYC
* [API][Customer] Create customer
* [API][CASA] Create CASA account - opening at "current_time_stamp" with product version id "official_product_version_id"
* [API][PostingInstruction] Inbound Hard Settlement at time stamp "current_time_stamp" with data - amount "1000000000" - account id "current_account_id" - transaction code "VIKKI_TO_NAPAS,E_BANKING,CASA"
* [API][PostingInstruction] Get balance and info of "current_account_id", then transfer at time stamp "current_time_stamp" with data - amount "20000000" - from account id "current_account_id" - to account id "default_account_id" - transaction code "VIKKI_TO_VIKKI,INTERNAL_TRANSFER,E_BANKING,CASA"
* [API][PostingInstruction] Get balance and info of "current_account_id", then transfer at time stamp "current_time_stamp" with data - amount "20000000" - from account id "current_account_id" - to account id "default_account_id" - transaction code "VIKKI_TO_HDBANK,INTERNAL_TRANSFER,E_BANKING,CASA"
* [API][PostingInstruction] Get balance and info of "current_account_id", then transfer at time stamp "current_time_stamp" with data - amount "20000000" - from account id "current_account_id" - to account id "default_account_id" - transaction code "VIKKI_TO_NAPAS,E_BANKING,CASA"
* [API][CASA] Get CASA account with id "current_account_id"
* [API][Common] Sleep "2" seconds
* [API][Flag] Grant VKYC for customer id "current_customer_id"
* [API][Common] Sleep "5" seconds

## Verify daily/monthly limit - card
* [API][CASA] Verify account EKYC - daily limit of CASA account with id "current_account_id" should be correct after upgrading to VKYC
* [API][CASA] Verify account EKYC - "monthly" limit - "E_BANKING" of CASA account with id "current_account_id" should be correct as "-1" after upgrading to VKYC
* [API][CASA] Verify account EKYC - "monthly" limit - "CARD" of CASA account with id "current_account_id" should be correct as "200000000" after upgrading to VKYC
* [API][CASA] Verify account EKYC - "monthly" limit - "CASA" of CASA account with id "current_account_id" should be correct as "-1" after upgrading to VKYC

## Create Customer > Account > Inbound balance > Get balance and info > Make different trx to reduce limit > Grant VKYC
* [API][Customer] Create customer
* [API][CASA] Create CASA account - opening at "current_time_stamp" with product version id "official_product_version_id"
* [API][PostingInstruction] Inbound Hard Settlement at time stamp "current_time_stamp" with data - amount "1000000000" - account id "current_account_id" - transaction code "VIKKI_TO_NAPAS,E_BANKING,CASA"
* [API][PostingInstruction] Get balance and info of "current_account_id", then transfer at time stamp "current_time_stamp" with data - amount "20000000" - from account id "current_account_id" - to account id "default_account_id" - transaction code "VIKKI_TO_VIKKI,INTERNAL_TRANSFER,E_BANKING,CASA"
* [API][PostingInstruction] Get balance and info of "current_account_id", then transfer at time stamp "current_time_stamp" with data - amount "20000000" - from account id "current_account_id" - to account id "default_account_id" - transaction code "VIKKI_TO_HDBANK,INTERNAL_TRANSFER,E_BANKING,CASA"
* [API][PostingInstruction] Get balance and info of "current_account_id", then transfer at time stamp "current_time_stamp" with data - amount "20000000" - from account id "current_account_id" - to account id "default_account_id" - transaction code "VIKKI_TO_NAPAS,E_BANKING,CASA"
* [API][PostingInstruction] Get balance and info of "current_account_id", then Outbound Hard Settlement at time stamp "current_time_stamp" with data - amount "20000000" - account id "current_account_id" - transaction code "VIRTUAL_CARD_CARD_NOT_PRESENT,CARD,CASA"
* [API][CASA] Get CASA account with id "current_account_id"
* [API][Common] Sleep "2" seconds
* [API][Flag] Grant VKYC for customer id "current_customer_id"
* [API][Common] Sleep "5" seconds

## Verify daily/monthly limit - all
* [API][CASA] Verify account EKYC - daily limit of CASA account with id "current_account_id" should be correct after upgrading to VKYC
* [API][CASA] Verify account EKYC - monthly limit of CASA account with id "current_account_id" should be correct after upgrading to VKYC