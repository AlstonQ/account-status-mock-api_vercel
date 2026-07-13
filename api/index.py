from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Any, Dict, Iterable, Optional

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

ACCOUNT_SCENARIOS = {
    "10010100463337": {
        "acct_name": "ARJUN S",
        "mobile": "919656568238",
        "status": "A",
        "account_closed": "N",
        "account_freezed": " ",
        "lien_marking": "0",
        "clr_balance": "11131.6",
        "freetext1": "S000",
        "freetext2": "SUCCESS"
    },
    "10010100463338": {
        "acct_name": "REENA JOSE",
        "mobile": "919656568239",
        "status": "C",
        "account_closed": "Y",
        "account_close_date": "2024-04-30",
        "clr_balance": "0",
        "freetext1": "F001",
        "freetext2": "Account is closed in Finacle"
    },
    "10010100463339": {
        "acct_name": "VIKRAM MENON",
        "mobile": "919656568240",
        "status": "F",
        "account_closed": "N",
        "account_freezed": "T",
        "freeze_reason_code": "DRFZ",
        "clr_balance": "8742.2",
        "freetext1": "F002",
        "freetext2": "Account is frozen in Finacle"
    },
    "10010100463340": {
        "acct_name": "PRIYA NAIR",
        "mobile": "919656568241",
        "status": "A",
        "account_closed": "N",
        "lien_marking": "1",
        "clr_balance": "24750.75",
        "freetext1": "F003",
        "freetext2": "Lien marked on account in Finacle"
    }
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

def has_empty_required(values: Iterable[Optional[str]]) -> bool:
    return any(value is None or str(value).strip() == "" for value in values)

def is_numeric(value: Optional[str]) -> bool:
    return value is not None and str(value).isdigit()

def scenario_text(*values: Optional[str]) -> str:
    return " ".join(str(value).lower() for value in values if value)

def with_request_id(response: Dict[str, Any], request_id: str) -> Dict[str, Any]:
    payload = response.copy()
    payload["requestId"] = request_id
    return payload

def account_status_response(request: AccountStatusRequest) -> Dict[str, Any]:
    if has_empty_required([request.channel, request.acctId, request.mobile, request.channelRequesetId]):
        payload = FAILURE_RESPONSE.copy()
        payload["freetext1"] = "F000"
        payload["freetext2"] = "Mandatory parameters missing"
        return payload

    account = ACCOUNT_SCENARIOS.get(request.acctId)
    if not account:
        payload = FAILURE_RESPONSE.copy()
        payload["freetext1"] = "F004"
        payload["freetext2"] = "Account not found in Finacle"
        return payload

    if account["mobile"] != request.mobile:
        payload = FAILURE_RESPONSE.copy()
        payload["account_number"] = request.acctId
        payload["freetext1"] = "F005"
        payload["freetext2"] = "Mobile number mismatch in Finacle"
        return payload

    payload = SUCCESS_RESPONSE.copy()
    payload.update(account)
    payload.pop("mobile", None)
    payload["account_number"] = request.acctId
    return payload

def nominee_finacle_response(request: NomineeUpdateRequest) -> Dict[str, Any]:
    req_type = request.reqType.upper()
    scenario = scenario_text(request.requestId, request.foracid, request.reserveFreetext1, request.reserveFreetext10)

    if not request.requestId:
        return with_request_id(NOMINEE_FAILURE_RESPONSE, request.requestId)

    if req_type not in {"ADD", "ENQUIRY"}:
        payload = NOMINEE_FAILURE_RESPONSE.copy()
        payload["message"] = "Invalid request type"
        return with_request_id(payload, request.requestId)

    if req_type == "ENQUIRY":
        if "fail" in scenario or "reject" in scenario:
            payload = NOMINEE_FAILURE_RESPONSE.copy()
            payload["message"] = "Nominee updation failed in Finacle"
            payload["cbsStatus"] = "FAILURE"
            payload["cbsResponse"] = "Finacle rejected nominee update request"
            return with_request_id(payload, request.requestId)

        payload = NOMINEE_ENQUIRY_RESPONSE.copy()
        payload["cbsStatus"] = "SUCCESS"
        payload["cbsResponse"] = "Nominee details updated successfully in Finacle"
        return with_request_id(payload, request.requestId)

    if has_empty_required([
        request.foracid,
        request.serviceReqId,
        request.EKYCrrn,
        request.nomineeName,
        request.nomineeRegno,
        request.nomineeRelType,
        request.nomineeMinorFlag,
        request.nomineeDob,
        request.nomineeAddrLine1,
        request.nomineeCity,
        request.nomineeState,
        request.nomineeCountry,
        request.nomineePostalCode,
        request.channel
    ]):
        return with_request_id(NOMINEE_FAILURE_RESPONSE, request.requestId)

    if not is_numeric(request.foracid) or len(request.foracid) != 14:
        payload = NOMINEE_FAILURE_RESPONSE.copy()
        payload["message"] = "Unknown error occured, please check the parameters"
        return with_request_id(payload, request.requestId)

    if request.nomineeMinorFlag.upper() == "Y" and has_empty_required([request.guardianCode, request.guardianName]):
        payload = NOMINEE_FAILURE_RESPONSE.copy()
        payload["message"] = "Guardian details are mandatory for minor nominee"
        return with_request_id(payload, request.requestId)

    if "duplicate" in scenario:
        payload = NOMINEE_FAILURE_RESPONSE.copy()
        payload["message"] = "Duplicate insert not allowed"
        return with_request_id(payload, request.requestId)

    if "cbsfail" in scenario or "reject" in scenario:
        payload = NOMINEE_FAILURE_RESPONSE.copy()
        payload["message"] = "Nominee update rejected by Finacle"
        payload["cbsStatus"] = "FAILURE"
        payload["cbsResponse"] = "Invalid nominee relationship code"
        return with_request_id(payload, request.requestId)

    payload = NOMINEE_SUCCESS_RESPONSE.copy()
    payload["status"] = "A000"
    payload["message"] = "Request received for Nominee updation"
    payload["cbsStatus"] = "PENDING"
    payload["cbsResponse"] = "Request posted to Finacle"
    return with_request_id(payload, request.requestId)

def profile_finacle_response(request: ProfileUpdateRequest) -> Dict[str, Any]:
    req_type = request.reqType.upper()
    scenario = scenario_text(request.requestId, request.customerId, request.reserveFreetext10)

    if not request.requestId:
        return with_request_id(PROFILE_FAILURE_RESPONSE, request.requestId)

    if req_type not in {"ADD", "ENQUIRY"}:
        payload = PROFILE_FAILURE_RESPONSE.copy()
        payload["status"] = "ERR0"
        payload["message"] = "Invalid request type"
        return with_request_id(payload, request.requestId)

    if req_type == "ENQUIRY":
        if "fail" in scenario or "reject" in scenario:
            payload = PROFILE_FAILURE_RESPONSE.copy()
            payload["CustomerID"] = request.customerId
            payload["cbsStatus"] = "FAILURE"
            payload["cbsResponse"] = "Retail customer update failed in Finacle"
            return with_request_id(payload, request.requestId)

        payload = PROFILE_ENQUIRY_RESPONSE.copy()
        payload["CustomerID"] = request.customerId or "22385796"
        payload["cbsResponse"] = f"Retail Customer successfully updated with CIFID {payload['CustomerID']}"
        return with_request_id(payload, request.requestId)

    if has_empty_required([request.channelId, request.customerId]):
        return with_request_id(PROFILE_FAILURE_RESPONSE, request.requestId)

    if not is_numeric(request.customerId) or len(request.customerId) > 10:
        payload = PROFILE_FAILURE_RESPONSE.copy()
        payload["status"] = "ERR0"
        payload["message"] = "Unknown error occurred, please check the parameters"
        return with_request_id(payload, request.requestId)

    if "duplicate" in scenario:
        payload = PROFILE_FAILURE_RESPONSE.copy()
        payload["status"] = "F001"
        payload["message"] = "Duplicate insert not allowed"
        payload["CustomerID"] = request.customerId
        return with_request_id(payload, request.requestId)

    if "cbsfail" in scenario or "reject" in scenario:
        payload = PROFILE_FAILURE_RESPONSE.copy()
        payload["CustomerID"] = request.customerId
        payload["cbsStatus"] = "FAILURE"
        payload["cbsResponse"] = "KYC update rejected by Finacle"
        return with_request_id(payload, request.requestId)

    payload = PROFILE_SUCCESS_RESPONSE.copy()
    payload["status"] = "A000"
    payload["message"] = "Request received for Profile updation"
    payload["CustomerID"] = request.customerId
    payload["cbsStatus"] = "PENDING"
    payload["cbsResponse"] = "Request posted to Finacle"
    return with_request_id(payload, request.requestId)

@app.post("/restgateway/services/AccountStatusEnquiry/acctStatusEnq")
def account_status_enquiry(request: AccountStatusRequest):
    return account_status_response(request)

@app.post("/restgateway/services/account/nomineeUpdate")
def nominee_update(request: NomineeUpdateRequest):
    return nominee_finacle_response(request)

@app.post("/restgateway/services/profileUpdateService")
def profile_update(request: ProfileUpdateRequest):
    return profile_finacle_response(request)