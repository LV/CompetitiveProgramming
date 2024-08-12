# Compiler
CXX := g++

# Compiler flags
CXXFLAGS := -std=c++11 -Wall -Wextra

# Rule to compile and run any C++ file
%: %.cpp
	@echo "Compiling $<..."
	@$(CXX) $(CXXFLAGS) $< -o $@
	@echo "Running $@..."
	@./$@
	@echo "Cleaning up..."
	@rm $@

.PHONY: clean

clean:
	@echo "Cleaning up..."
	@rm -f $(wildcard *.o) $(wildcard *.out)
