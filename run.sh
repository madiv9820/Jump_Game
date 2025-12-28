#!/bin/bash

# ============================================================
# 🚀 Independent Test Runner (Python & C++)
# ============================================================

PYTHON_STATUS=0
CPP_STATUS=0

echo "🐍 Creating Python virtual environment..."
python3 -m venv venv
echo "✅ Virtual environment created!"

echo "⚡ Activating virtual environment..."
source ./venv/bin/activate
echo "🟢 Virtual environment activated!"

echo "📦 Installing required Python libraries..."
pip install -r requirements.txt
echo "✅ Dependencies installed!"

# ------------------------------------------------------------
# 🧪 Python Tests (Independent)
# ------------------------------------------------------------
echo "🧪 Running Python test cases..."
if python -m test.py_test -v; then
    echo "✅ Python tests PASSED 🎉"
else
    echo "❌ Python tests FAILED 😞"
    PYTHON_STATUS=1
fi

# ------------------------------------------------------------
# ⚙️ Build C++ Extension (Independent)
# ------------------------------------------------------------
echo "⚙️ Building C++ extension..."
cd ./source/cpp 
if python setup.py build_ext --inplace; then
    echo "✅ C++ extension built!"
else
    echo "❌ C++ build FAILED 🧨"
    CPP_STATUS=1
fi

cd ../..

# ------------------------------------------------------------
# 🧪 C++ Tests (Independent)
# ------------------------------------------------------------
echo "🧪 Running C++ test cases..."
if python -m test.cpp_test -v; then
    echo "✅ C++ tests PASSED 🚀"
else
    echo "❌ C++ tests FAILED 😞"
    CPP_STATUS=1
fi

# ------------------------------------------------------------
# 🔚 Cleanup
# ------------------------------------------------------------
echo "👋 Deactivating virtual environment..."
deactivate

# ------------------------------------------------------------
# 📊 Final Summary
# ------------------------------------------------------------
echo ""
echo "================ 🧾 TEST SUMMARY 🧾 ================"

if [ $PYTHON_STATUS -eq 0 ]; then
    echo "🐍 Python Tests : ✅ PASSED"
else
    echo "🐍 Python Tests : ❌ FAILED"
fi

if [ $CPP_STATUS -eq 0 ]; then
    echo "⚙️ C++ Tests    : ✅ PASSED"
else
    echo "⚙️ C++ Tests    : ❌ FAILED"
fi

echo "==================================================="

# ------------------------------------------------------------
# 🔔 Exit Code (CI Friendly)
# ------------------------------------------------------------
if [ $PYTHON_STATUS -ne 0 ] || [ $CPP_STATUS -ne 0 ]; then
    echo "❌ Some tests failed. Please fix them 🛠️"
    exit 1
else
    echo "🎉 All tests passed successfully! Great job 💪"
    exit 0
fi