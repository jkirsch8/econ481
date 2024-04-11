{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8908fbb7-4477-4664-be71-34dd20680ae3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Problem 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "02e4daea-7fb9-43c4-8585-732e2e5d9408",
   "metadata": {},
   "outputs": [],
   "source": [
    "def github() -> str:\n",
    "    \"\"\"\n",
    "    Returns a link to this file in my github repository\n",
    "    \"\"\"\n",
    "\n",
    "    return \"https://github.com/jkirsch8/econ481/blob/main/HW2.py\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "04d43222-56f8-43e3-b6ef-ec8a4d2c4a2c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Problem 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "11cfdb66-87ef-4b9f-b227-343f1f7c4d16",
   "metadata": {},
   "outputs": [],
   "source": [
    "def simulate_data(seed = 481) -> tuple:\n",
    "    \"\"\"\n",
    "    Generates 1000 simulations following the distribution y = 5 + 3x1 + 2x2 + 6x3 + e\n",
    "    \"\"\"\n",
    "    import numpy as np\n",
    "    rng = np.random.default_rng(seed = seed)\n",
    "    draws = rng.normal(0,np.sqrt(2),3000)\n",
    "    x = draws.reshape(1000,3)\n",
    "    e = rng.standard_normal(1000).reshape(1000,1)\n",
    "    ints = np.ones(1000).reshape(1000,1)\n",
    "    array = np.concatenate((ints,x,e),axis=1)\n",
    "    beta = [5,3,2,6,1]\n",
    "    y = array @ beta\n",
    "    y = y.reshape(1000,1)\n",
    "    return (y,x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "4b78e656-d6a9-46d7-850b-4f4552a66a54",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5.407028730585224"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y,x = simulate_data()\n",
    "import numpy as np\n",
    "np.mean(y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "40eb2291-aca0-4f3d-873d-3d4aebe90e0e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Problem 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "8d6e4fc3-8886-45be-9646-97e3797bc13c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def neg_ll(beta,y,x) -> np.array:\n",
    "    \"\"\"\n",
    "    Compute the negative log-likelihood for the distribution of errors for given data and beta estimates\n",
    "    \"\"\"\n",
    "    beta = beta.reshape(-1,1)\n",
    "    x_ints = np.c_[np.ones(x.shape[0]).reshape(-1,1),x]\n",
    "    e = np.abs(y - x_ints @ beta)\n",
    "    p = 2*sp.stats.norm.sf(e)\n",
    "    value = sum(np.log(p))\n",
    "    return -1*value\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "53efc131-eaf8-498a-8577-df9f720e2a99",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import scipy as sp\n",
    "\n",
    "def estimate_mle(y: np.array, x: np.array) -> np.array:\n",
    "    \"\"\"\n",
    "    Estimates the MLE parameters for given data\n",
    "    \"\"\"\n",
    "    result = sp.optimize.minimize(\n",
    "        fun = neg_ll,\n",
    "        x0 = (1,1,1,1),\n",
    "        args = (y,x),\n",
    "        bounds = ((1,10),(1,10),(1,10),(1,10)),\n",
    "        method = 'Nelder-Mead')\n",
    "    return result.x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "0608c4b1-5424-414e-8a7d-b90d68962df7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([4.95281893, 3.01002521, 1.99496124, 6.00521595])"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "estimate_mle(*simulate_data())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "d0f403d3-dda8-4421-a86c-0c9375a91621",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Problem 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "137bdca4-71a1-4bcf-9320-c12a30f9a2a1",
   "metadata": {},
   "outputs": [],
   "source": [
    "def sse(beta,y,x) -> float:\n",
    "    \"\"\"\n",
    "    computes the sum of squared errors for given data and estimates of coefficients\n",
    "    \"\"\"\n",
    "    beta = beta.reshape(-1,1)\n",
    "    x_ints = np.c_[np.ones(x.shape[0]).reshape(-1,1),x]\n",
    "    e = y - x_ints @ beta\n",
    "    sse =  e.T @ e\n",
    "    return sse"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "fb0e8f87-b767-43b7-82ce-0ad973999a19",
   "metadata": {},
   "outputs": [],
   "source": [
    "def estimate_ols(y: np.array, x: np.array) -> np.array:\n",
    "    \"\"\"\n",
    "    Estimates the OLS coefficients for given data by minimizing sum of squared errors\n",
    "    \"\"\"\n",
    "    \n",
    "    import scipy as sp\n",
    "    result = sp.optimize.minimize(\n",
    "        fun = sse,\n",
    "        x0 = (1,1,1,1),\n",
    "        args = (y,x),\n",
    "        method = 'Nelder-Mead'\n",
    "    )\n",
    "    return result.x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "e5f081e2-e285-4f40-a644-7ca9ffe4e954",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([4.95062832, 2.98614707, 1.99109057, 6.00663598])"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "estimate_ols(*simulate_data())"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
