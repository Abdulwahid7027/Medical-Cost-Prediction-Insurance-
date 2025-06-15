import React from 'react';
import PredictionForm from './PredictionForm';
import { motion } from 'framer-motion';

function App() {
  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center">
      <motion.div
        initial={{ opacity: 0, y: -50 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8 }}
        className="text-center mb-8"
      >
        <h1 className="text-4xl font-bold text-primary">Medical Cost Prediction</h1>
        <p className="text-lg text-gray-600 mt-2">Estimate your annual insurance costs with AI</p>
      </motion.div>
      <PredictionForm />
    </div>
  );
}

export default App;