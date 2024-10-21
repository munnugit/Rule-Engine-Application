import React from 'react';
import RuleForm from './components/RuleForm';
import EvaluateForm from './components/EvaluateForm';

const App = () => {
    return (
        <div>
            <h1>Rule Engine Application</h1>
            <RuleForm />
            <EvaluateForm />
        </div>
    );
};

export default App;
