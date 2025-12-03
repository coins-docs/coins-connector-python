def sellorder_new(self, payment_outlet='', currency='', base_amount='', bank_account_number='', bank_account_name='', recipient_phone_number=''):
    params = {}
    if base_amount:
        params['base_amount'] = base_amount
    if currency:
        params['currency'] = currency
    if bank_account_number:
        params['bank_account_number'] = bank_account_number
    if bank_account_name:
        params['bank_account_name'] = bank_account_name
    if recipient_phone_number:
        params['recipient_phone_number'] = recipient_phone_number
    if payment_outlet:
        params['payment_outlet'] = payment_outlet
    return self._post('openapi/migration/v4/sellorder', signed=True, data=params)


def sellorder_query(self, sell_order_id=''):
    params = {}
    path = 'openapi/migration/v4/sellorder'
    if sell_order_id:
        path = path + '/' + sell_order_id
    return self._get(path, signed=True, params=params)


def validate_field(self, field_type='', account_number='', account_type='', mobile_number='', region=''):
    params = {}
    if field_type:
        params['field_type'] = field_type
    if account_number:
        params['account_number'] = account_number
    if account_type:
        params['account_type'] = account_type
    if mobile_number:
        params['mobile_number'] = mobile_number
    if region:
        params['region'] = region
    return self._post('openapi/migration/v4/validate-field', signed=True, data=params)


def payout_outlets(self, outlet_category='', name='', region='', is_enabled='', id=''):
    params = {}
    if outlet_category:
        params['outlet_category'] = outlet_category
    if name:
        params['name'] = name
    if region:
        params['region'] = region
    if is_enabled:
        params['is_enabled'] = is_enabled
    if id:
        params['id'] = id
    return self._get('openapi/migration/v4/payout-outlets', signed=True, params=params)


def payout_outlet_categories(self, id=''):
    params = {}
    path = 'openapi/migration/v4/payout-outlet-categories'
    if id:
        path = path + '/' + id
    return self._get(path, signed=True, params=params)


def payout_outlet_fees(self, payment_outlet='', currency=''):
    params = {}
    if payment_outlet:
        params['payment_outlet'] = payment_outlet
    if currency:
        params['currency'] = currency
    return self._get('openapi/migration/v4/payout-outlet-fees', signed=True, params=params)
