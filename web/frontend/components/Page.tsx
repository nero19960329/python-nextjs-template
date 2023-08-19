import { useState } from "react";
import { useMutation, useQuery, useQueryClient } from "react-query";
import { getTests, postTest } from "../core/api";
import { Test } from "../core/types";

export const Page = () => {
  const query = useQuery("test", getTests);
  const [formVal, setFormVal] = useState<string>("");

  const queryClient = useQueryClient();

  const onSubmit = (event: any) => {
    event.preventDefault();

    const test: Test = { field_1: formVal };
    if (formVal.length > 0) {
      createTestMutation.mutate(test);
      setFormVal("");
    }
  };

  const createTestMutation = useMutation(postTest, {
    onSuccess: () => {
      queryClient.invalidateQueries("test");
    },
  });

  return (
    <>
      <p className="text-xl font-bold mb-4">Tests:</p>
      <ul className="list-disc ml-6">
        {query.data?.map((test: Test) => (
          <li key={test["field_1"]} className="mb-2">
            {test["field_1"]}
          </li>
        ))}
      </ul>

      <form className="mt-4">
        <label htmlFor="field1" className="block mb-2">
          Test field 1:
        </label>
        <input
          type="text"
          onChange={(e: any) => setFormVal(e.target.value)}
          value={formVal}
          id="field1"
          name="field1"
          className="border border-gray-300 rounded px-2 py-1 mb-2"
        />
        <button
          type="button"
          onClick={onSubmit}
          className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
        >
          Add a new test
        </button>
      </form>
    </>
  );
};
