from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Any, Dict, Optional

app = FastAPI()

class AccountStatusRequest(BaseModel):
    channel: str = Field(..., title="Channel name")
    acctId: str = Field(..., title="Account Number / Customer ID")
    mobile: str = Field(..., title="Mobile Number")
    channelRequesetId: str = Field(..., title="Channel Request ID")
    input1: Optional[str] = ""
    input2: Optional[str] = ""
    input3: Optional[str] = ""
    input4: Optional[str] = ""
    input5: Optional[str] = ""

class NomineeUpdateRequest(BaseModel):
    reqType: str = Field(..., title="ADD / ENQUIRY")
    foracid: Optional[str] = ""
    requestId: str = Field(..., title="Unique request id")
    serviceReqId: Optional[str] = ""
    EKYCrrn: Optional[str] = ""
    nomineeName: Optional[str] = ""
    nomineeRegno: Optional[str] = ""
    nomineeRelType: Optional[str] = ""
    nomineeMinorFlag: Optional[str] = ""
    nomineeDob: Optional[str] = ""
    nomineeAddrLine1: Optional[str] = ""
    nomineeAddrLine2: Optional[str] = ""
    nomineeAddrLine3: Optional[str] = ""
    nomineeCity: Optional[str] = ""
    nomineeState: Optional[str] = ""
    nomineeCountry: Optional[str] = ""
    nomineePostalCode: Optional[str] = ""
    guardianCode: Optional[str] = ""
    guardianName: Optional[str] = ""
    channel: str = Field(..., title="Channel")
    reserveFreetext1: Optional[str] = ""
    reserveFreetext2: Optional[str] = ""
    reserveFreetext3: Optional[str] = ""
    reserveFreetext4: Optional[str] = ""
    reserveFreetext5: Optional[str] = ""
    reserveFreetext6: Optional[str] = ""
    reserveFreetext7: Optional[str] = ""
    reserveFreetext8: Optional[str] = ""
    reserveFreetext9: Optional[str] = ""
    reserveFreetext10: Optional[str] = ""

class ProfileUpdateRequest(BaseModel):
    requestId: str = Field(..., title="Unique request id")
    channelId: Optional[str] = ""
    customerId: Optional[str] = ""
    reqType: str = Field(..., title="ADD / ENQUIRY")
    EKYCrrn: Optional[str] = ""
    DOB: Optional[str] = ""
    addrCategory: Optional[str] = ""
    addrLine1: Optional[str] = ""
    addrLine2: Optional[str] = ""
    cityCode: Optional[str] = ""
    stateCode: Optional[str] = ""
    countryCode: Optional[str] = ""
    pinCode: Optional[str] = ""
    qualification: Optional[str] = ""
    incomeRangeFrom: Optional[str] = ""
    incomeRangeTo: Optional[str] = ""
    community: Optional[str] = ""
    caste: Optional[str] = ""
    occupation: Optional[str] = ""
    panNumber: Optional[str] = ""
    reserveFreetext1: Optional[str] = ""
    reserveFreetext2: Optional[str] = ""
    reserveFreetext3: Optional[str] = ""
    reserveFreetext4: Optional[str] = ""
    reserveFreetext5: Optional[str] = ""
    reserveFreetext6: Optional[str] = ""
    reserveFreetext7: Optional[str] = ""
    reserveFreetext8: Optional[str] = ""
    reserveFreetext9: Optional[str] = ""
    reserveFreetext10: Optional[str] = ""

SUCCESS_RESPONSE = {
    "account_number": "10010100463337",
    "account_closed": "N",
    "account_freezed": " ",
    "lien_marking": "0",
    "sol_id": "1001",
    "scheme_code": "35006",
    "clr_balance": "11131.6",
    "freeze_reason_code": " ",
    "freeze_reason_code2": "",
    "freeze_reason_code3": "",
    "freeze_reason_code4": "",
    "freeze_reason_code5": "",
    "account_open_date": "2019-07-31",
    "account_close_date": "",
    "drawing_power": "0",
    "sanction_limit": "0",
    "adhoc_limit": "0",
    "cumulative_Dr_Amount": "255911.9",
    "cumulative_Cr_Amount": "267043.5",
    "last_trans_date": "2019-11-20",
    "account_currency_code": "INR",
    "scheme_type": "SBA",
    "cif_id": "128648335",
    "bank_Id": "01",
    "last_tran_date_CR": "2019-11-18",
    "last_tran_date_DR": "2019-11-20",
    "last_tran_id_CR": "S36432543",
    "last_tran_id_dr": "S40607977",
    "un_cleared_bal_amount": "0",
    "mode_of_operationCode": "SG",
    "cust_id": "128648335",
    "acct_name": "ARJUN S",
    "kycflag": "1",
    "status": "A",
    "last_tran_Amt_DR": "400",
    "last_tran_Amt_CR": "16",
    "signcount": "Y",
    "freetext1": "",
    "freetext2": "",
    "freetext3": "",
    "freetext4": "",
    "freetext5": "",
    "freetext6": "",
    "freetext7": "",
    "freetext8": "",
    "freetext9": "",
    "freetext10": "",
    "freetext11": "",
    "freetext12": "",
    "freetext14": "",
    "freetext15": "",
    "freetext16": "",
    "freetext17": "",
    "freetext18": "",
    "freetext19": "",
    "freetext20": ""
}

FAILURE_RESPONSE = {
    "account_number": "",
    "account_closed": "",
    "account_freezed": "",
    "lien_marking": "",
    "sol_id": "",
    "scheme_code": "",
    "clr_balance": "",
    "freeze_reason_code": " ",
    "freeze_reason_code2": "",
    "freeze_reason_code3": "",
    "freeze_reason_code4": "",
    "freeze_reason_code5": "",
    "account_open_date": "",
    "account_close_date": "",
    "drawing_power": "",
    "sanction_limit": "",
    "adhoc_limit": "",
    "cumulative_Dr_Amount": "",
    "cumulative_Cr_Amount": "",
    "last_trans_date": "",
    "account_currency_code": "",
    "scheme_type": "",
    "cif_id": "",
    "bank_Id": "",
    "last_tran_date_CR": "",
    "last_tran_date_DR": "",
    "last_tran_id_CR": "",
    "last_tran_id_dr": "",
    "un_cleared_bal_amount": "",
    "mode_of_operationCode": "",
    "cust_id": "",
    "acct_name": "",
    "kycflag": "",
    "status": "",
    "last_tran_Amt_DR": "",
    "last_tran_Amt_CR": "",
    "signcount": "",
    "freetext1": "0000",
    "freetext2": "Unknown error occured, please check the parameters",
    "freetext3": "",
    "freetext4": "",
    "freetext5": "",
    "freetext6": "",
    "freetext7": "",
    "freetext8": "",
    "freetext9": "",
    "freetext10": "",
    "freetext11": "",
    "freetext12": "",
    "freetext14": "",
    "freetext15": "",
    "freetext16": "",
    "freetext17": "",
    "freetext18": "",
    "freetext19": "",
    "freetext20": ""
}

NOMINEE_SUCCESS_RESPONSE = {
    "requestId": "",
    "status": "S000",
    "message": "Record inserted for Nominee updation",
    "cbsResponse": "",
    "cbsStatus": ""
}

NOMINEE_ENQUIRY_RESPONSE = {
    "requestId": "",
    "status": "S000",
    "message": "SUCCESS",
    "cbsResponse": "",
    "cbsStatus": ""
}

NOMINEE_FAILURE_RESPONSE = {
    "requestId": "",
    "status": "F001",
    "message": "Some error occured, please check the parameters",
    "cbsResponse": "",
    "cbsStatus": ""
}

PROFILE_SUCCESS_RESPONSE = {
    "requestId": "",
    "status": "S000",
    "message": "Record inserted for Profile updation",
    "CustomerID": "",
    "cbsStatus": "",
    "cbsResponse": ""
}

PROFILE_ENQUIRY_RESPONSE = {
    "requestId": "",
    "status": "S000",
    "message": "SUCCESS",
    "CustomerID": "",
    "cbsStatus": "SUCCESS",
    "cbsResponse": "Retail Customer successfully updated with CIFID 22385796"
}

PROFILE_FAILURE_RESPONSE = {
    "requestId": "",
    "status": "F000",
    "message": "Unknown error occurred, please check the parameters",
    "CustomerID": "",
    "cbsStatus": "",
    "cbsResponse": ""
}

def with_request_id(response: Dict[str, Any], request_id: str) -> Dict[str, Any]:
    payload = response.copy()
    payload["requestId"] = request_id
    return payload

@app.post("/restgateway/services/AccountStatusEnquiry/acctStatusEnq")
def account_status_enquiry(request: AccountStatusRequest):
    # Based on user feedback: Mock Logic returns success for exact matching parameters (e.g. mobile matches success request)
    if request.mobile == "919656568238":
        return SUCCESS_RESPONSE
    else:
        return FAILURE_RESPONSE

@app.post("/restgateway/services/account/nomineeUpdate")
def nominee_update(request: NomineeUpdateRequest):
    if not request.requestId:
        return with_request_id(NOMINEE_FAILURE_RESPONSE, request.requestId)

    if request.reqType.upper() == "ENQUIRY":
        return with_request_id(NOMINEE_ENQUIRY_RESPONSE, request.requestId)

    if request.reqType.upper() != "ADD" or not request.foracid or not request.channel:
        return with_request_id(NOMINEE_FAILURE_RESPONSE, request.requestId)

    return with_request_id(NOMINEE_SUCCESS_RESPONSE, request.requestId)

@app.post("/restgateway/services/profileUpdateService")
def profile_update(request: ProfileUpdateRequest):
    if not request.requestId:
        return with_request_id(PROFILE_FAILURE_RESPONSE, request.requestId)

    if request.reqType.upper() == "ENQUIRY":
        return with_request_id(PROFILE_ENQUIRY_RESPONSE, request.requestId)

    if request.reqType.upper() != "ADD" or not request.channelId or not request.customerId:
        return with_request_id(PROFILE_FAILURE_RESPONSE, request.requestId)

    return with_request_id(PROFILE_SUCCESS_RESPONSE, request.requestId)