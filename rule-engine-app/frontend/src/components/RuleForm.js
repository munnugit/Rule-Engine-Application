import React, { useState } from 'react';
import { createRule } from '../services/api';

const RuleForm = () => {
    const [rule, setRule] = useState('');

    const handleSubmit = async () => {
        const response = await createRule({ name: "Sample Rule", rule: rule });
        console.log(response.data);
    };

    return (
        <div>
            <input 
                type="text" 
                value={rule} 
                onChange={(e) => setRule(e.target.value)} 
                placeholder="Enter rule (e.g., age > 30 AND department = 'Sales')" 
            />
            <button onClick={handleSubmit}>Create Rule</button>
        </div>
    );
};

export default RuleForm;
