import React, { useState } from 'react';
import { useForm } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import * as Yup from 'yup';
import axios from 'axios';
import { motion } from 'framer-motion';
import ClipLoader from 'react-spinners/ClipLoader';

// Validation schema
const schema = Yup.object().shape({
  age: Yup.number()
    .typeError('Age must be a number')
    .required('Age is required')
    .min(18, 'Age must be at least 18')
    .max(100, 'Age cannot exceed 100'),
  sex: Yup.string().required('Sex is required'),
  bmi: Yup.number()
    .typeError('BMI must be a number')
    .required('BMI is required')
    .min(10, 'BMI must be at least 10')
    .max(50, 'BMI cannot exceed 50'),
  children: Yup.number()
    .typeError('Children must be a number')
    .required('Children is required')
    .min(0, 'Children cannot be negative')
    .max(10, 'Children cannot exceed 10'),
  smoker: Yup.string().required('Smoker status is required'),
  region: Yup.string().required('Region is required'),
});

const PredictionForm = () => {
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const {
    register,
    handleSubmit,
    formState: { errors },
    reset,
  } = useForm({
    resolver: yupResolver(schema),
    defaultValues: {
      age: '',
      sex: 'male',
      bmi: '',
      children: '',
      smoker: 'no',
      region: 'northeast',
    },
  });

  const onSubmit = async (data) => {
    setLoading(true);
    setPrediction(null);
    try {
      const response = await axios.post(process.env.REACT_APP_API_URL || 'http://localhost:5000/predict', {
        age: parseInt(data.age),
        sex: data.sex,
        bmi: parseFloat(data.bmi),
        children: parseInt(data.children),
        smoker: data.smoker,
        region: data.region,
      });
      setPrediction(response.data.prediction);
    } catch (err) {
      setPrediction({ error: err.response?.data?.message || 'Error making prediction' });
    } finally {
      setLoading(false);
    }
  };

  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.95 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{ duration: 0.5 }}
      className="bg-white p-8 rounded-xl shadow-2xl w-full max-w-md"
    >
      <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
        <div>
          <label className="block text-sm font-medium text-gray-700">Age</label>
          <input
            type="number"
            {...register('age')}
            className={`mt-1 block w-full px-3 py-2 border ${
              errors.age ? 'border-red-500' : 'border-gray-300'
            } rounded-md shadow-sm focus:outline-none focus:ring-primary focus:border-primary`}
          />
          {errors.age && <p className="mt-1 text-sm text-red-600">{errors.age.message}</p>}
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700">Sex</label>
          <select
            {...register('sex')}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-primary focus:border-primary"
          >
            <option value="male">Male</option>
            <option value="female">Female</option>
          </select>
          {errors.sex && <p className="mt-1 text-sm text-red-600">{errors.sex.message}</p>}
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700">BMI</label>
          <input
            type="number"
            step="0.1"
            {...register('bmi')}
            className={`mt-1 block w-full px-3 py-2 border ${
              errors.bmi ? 'border-red-500' : 'border-gray-300'
            } rounded-md shadow-sm focus:outline-none focus:ring-primary focus:border-primary`}
          />
          {errors.bmi && <p className="mt-1 text-sm text-red-600">{errors.bmi.message}</p>}
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700">Children</label>
          <input
            type="number"
            {...register('children')}
            className={`mt-1 block w-full px-3 py-2 border ${
              errors.children ? 'border-red-500' : 'border-gray-300'
            } rounded-md shadow-sm focus:outline-none focus:ring-primary focus:border-primary`}
          />
          {errors.children && <p className="mt-1 text-sm text-red-600">{errors.children.message}</p>}
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700">Smoker</label>
          <select
            {...register('smoker')}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-primary focus:border-primary"
          >
            <option value="yes">Yes</option>
            <option value="no">No</option>
          </select>
          {errors.smoker && <p className="mt-1 text-sm text-red-600">{errors.smoker.message}</p>}
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700">Region</label>
          <select
            {...register('region')}
            className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-primary focus:border-primary"
          >
            <option value="northeast">Northeast</option>
            <option value="northwest">Northwest</option>
            <option value="southeast">Southeast</option>
            <option value="southwest">Southwest</option>
          </select>
          {errors.region && <p className="mt-1 text-sm text-red-600">{errors.region.message}</p>}
        </div>

        <motion.button
          type="submit"
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
          className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-primary hover:bg-blue-900 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary"
          disabled={loading}
        >
          {loading ? (
            <ClipLoader color="#ffffff" size={20} />
          ) : (
            'Predict Cost'
          )}
        </motion.button>
      </form>

      {prediction && (
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
          className="mt-6 p-4 bg-green-50 rounded-md"
        >
          {prediction.error ? (
            <p className="text-red-600">{prediction.error}</p>
          ) : (
            <h3 className="text-lg font-semibold text-secondary">
              Predicted Annual Cost: ${prediction.toLocaleString()}
            </h3>
          )}
        </motion.div>
      )}
    </motion.div>
  );
};

export default PredictionForm;