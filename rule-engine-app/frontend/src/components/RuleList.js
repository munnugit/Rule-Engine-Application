import React, { useState } from 'react';
import { evaluateRule } from '../services/api';

const EvaluateForm = () => {
    const [userData, setUserData] = useState({ age: 35, department: 'Sales', salary: 60000, experience: 3 });

    const handleEvaluation = async () => {
        const response = await evaluateRule({ rule_id: 1, user_data: userData });
        console.log(response.data);
    };

    return (
        <div>
            <button onClick={handleEvaluation}>Evaluate Rule</button>
        </div>
    );
};

export default EvaluateForm;
