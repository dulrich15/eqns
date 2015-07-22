# Problem solving algorithm

- Let EQ represent a list of the equations of interest. Let v(EQ) represent the
  variables in the equations of EQ.
- Parse the question to identify all VOI (variables of interest).
- [Optional] Identify the context of the problem.
- Filter equation set to include only those equations with variables consistent
  with the list of VOI.
- Calculate v(EQ). Remove the VOI. Return to step 2 if non-empty.
- If the number of equations in EQ is greater than one, use context to break
  the tie.
- Verify context of the remaining equation. If this doesn't check, start over.
  Something is seriously wrong!
- Parse the question to identify the unknown and record the given data, whether
  explicit or implicit.
- Solve it and prosper!
