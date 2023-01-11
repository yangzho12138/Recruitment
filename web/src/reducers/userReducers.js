import { USER_LOGIN_REQUEST, USER_LOGIN_SUCCESS, USER_LOGIN_FAIL, USER_LOGOUT } from "../contants/userConstants"
import { USER_REGISTER_REQUEST, USER_REGISTER_SUCCESS, USER_REGISTER_FAIL } from "../contants/userConstants"
import { USER_RESUME_UPDATE_REQUEST, USER_RESUME_UPDATE_SUCCESS, USER_RESUME_UPDATE_FAIL } from "../contants/userConstants"
import { USER_RESUME_REQUEST, USER_RESUME_SUCCESS,USER_RESUME_FAIL } from "../contants/userConstants"

export const userLoginReducer = (state = {}, action) => {
    switch(action.type){
        case USER_LOGIN_REQUEST:
            return { loading: true }
        case USER_LOGIN_SUCCESS:
            return { loading: false, userInfo: action.payload }
        case USER_LOGIN_FAIL:
            return { loading: false, error: action.payload }
        case USER_LOGOUT:
            return {}
        default:
            return state
    }
}

export const userRegisterReducer = (state = {}, action) => {
    switch(action.type){
        case USER_REGISTER_REQUEST:
            return { loading: true }
        case USER_REGISTER_SUCCESS:
            return { loading: false }
        case USER_REGISTER_FAIL:
            return { loading: false, error: action.payload }
        default:
            return state
    }
}

export const userResumeReducer = (state = {}, action) => {
    switch(action.type){
        case USER_RESUME_REQUEST:
            return { loading: true }
        case USER_RESUME_SUCCESS:
            return { loading: false, userResume: action.payload }
        case USER_RESUME_FAIL:
            return { loading: false, error: action.payload }
        default:
            return state
    }
}

export const userResumeUpdateReducer = (state = {}, action) => {
    switch(action.type){
        case USER_RESUME_UPDATE_REQUEST:
            return { loading: true }
        case USER_RESUME_UPDATE_SUCCESS:
            return { loading: false, userResume: action.payload }
        case USER_RESUME_UPDATE_FAIL:
            return { loading: false, error: action.payload }
        default:
            return state
    }
}