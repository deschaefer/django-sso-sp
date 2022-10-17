# django-sso-sp

openssl req -nodes -new -x509 -newkey rsa:2048 -days 3650 -keyout private.key -out public.cert

subject: the athenaNet user’s username
practiceID: this is the same ID used for the API
departmentID: this is the ID of the department the user is logged into and clicking the link from 
email: available only if filled out. This is not a required field in athenaNet 
firstName: the athenaNet user’s first name 
lastName: the athenaNet user’s last name 
fullName: the athenaNet user’s first and last name 
patient_id: The patientID sent only when the SSO link is located and activated from a patient-centric page within athenaNet. It is not sent from all SSO links in athenaNet. Please refer to the location descriptions below to see which include this information. 
usertype: The current user’s type (‘employee’ or ‘client’) 
position: The current user’s position within the practice (ex. “Provider”, “Clinical Staff”, etc.) This is not a required field in athenaNet. 
extraidentifier: A configurable string of data that can be passed within the call. 
This is typically used to send the encounterID information. 


subject
practiceID
departmentID 
email 
firstName 
lastName 
fullName 
patient_id
usertype
position 
extraidentifier 


https://staging.anodyneclinical.com/saml2/acs/

{
// "audience":  "urn:foo",
// "recipient": "http://foo",
 "mappings": {
   "user_id":     "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/subject",
   "email":       "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/email",
   "name":        "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/fullName",
   "given_name":  "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/firstName",
   "family_name": "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/lastName",
//   "upn":         "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/upn",
//   "groups":      "http://schemas.xmlsoap.org/claims/Group"
 },
 "createUpnClaim":       false,
 "passthroughClaimsWithNoMapping": true,
 "mapUnknownClaimsAsIs": true,
 "mapIdentities":        true,
 "signatureAlgorithm":   "sha256",
 "digestAlgorithm":      "sha256",
// "destination":          "http://foo",
// "lifetimeInSeconds":    3600,
// "signResponse":         false,
// "typedAttributes":      true,
// "includeAttributeNameFormat":  true,
// "nameIdentifierFormat": "urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified",
// "nameIdentifierProbes": [
//   "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier",
//   "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress",
//   "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name"
// ],
// "authnContextClassRef": "urn:oasis:names:tc:SAML:2.0:ac:classes:unspecified",
 "logout": {
   "callback": "http://staging.anodyneclinical.com/saml2/ls/post",
   "slo_enabled": true
 },
 "binding": "urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST"
}


SAML Protocol Configuration Parameters
SAML Version: 2.0
Issuer: urn:dev-wat-m0kt.us.auth0.com
Identity Provider Certificate: Download Auth0 certificate
Identity Provider SHA1 fingerprint: 0C:55:54:0C:BE:C6:03:DD:E3:30:19:9B:80:86:B8:B8:DD:BD:3A:9A
Identity Provider Login URL: https://dev-wat-m0kt.us.auth0.com/samlp/iJQKjNUfWHzycGhZN5dRBbxLcl7REuyl
Identity Provider Metadata: Download
Alternatively, you can add a connection parameter:

https://dev-wat-m0kt.us.auth0.com/samlp/iJQKjNUfWHzycGhZN5dRBbxLcl7REuyl?connection=google-oauth2
https://dev-wat-m0kt.us.auth0.com/samlp/iJQKjNUfWHzycGhZN5dRBbxLcl7REuyl?connection=Username-Password-Authentication
