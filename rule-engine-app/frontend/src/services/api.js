import axios from 'axios';

const api = axios.create({
    baseURL: 'http://localhost:5000/api'
});

export const createRule = (rule) => api.post('/create_rule', rule);
export const evaluateRule = (evaluationData) => api.post('/evaluate_rule', evaluationData);
export const combineRules = (ruleData) => api.post('/combine_rules', ruleData);
