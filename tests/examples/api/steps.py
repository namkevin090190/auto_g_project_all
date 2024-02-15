from platforms import step
from .petstore import PetStore

from cores.utils import GetUtil, StoreUtil, AssertUtil
from cores.model.request import ResponseObj


@step('Create new pet')
def step_create_new_pet():
    r = PetStore.create_pet()
    StoreUtil.scenario_store('pet_response', r)
    return r


@step('Retrieve Pet infomation <pet_id>')
def step_retrieve_pet_info(pet_id=None):
    pet_id = GetUtil.scenario_get('pet_response')['id'] if pet_id in ('', 'none') else pet_id
    r = PetStore.retrieve_pet_info(pet_id=pet_id)
    StoreUtil.scenario_store('info_response', r)


#######
# Verification
#######

@step('Verify created pet successfully')
def step_verify_create_pet():
    res: ResponseObj = GetUtil.scenario_get('pet_response')
    verify = AssertUtil
    verify.true(res['id'])  # create successfully
    verify.equal(res['status'], 'available')  # message


@step('Verfiy retrive pet info successfully <pet_id>')
def step_verify_get_info(pet_id=None):
    pet_id = GetUtil.scenario_get('pet_response')['id'] if pet_id in ('', 'none') else pet_id
    res = GetUtil.scenario_get('info_response')
    AssertUtil.equal(pet_id, res['id'])
