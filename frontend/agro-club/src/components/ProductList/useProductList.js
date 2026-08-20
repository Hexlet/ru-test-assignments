import { useCallback, useEffect, useReducer } from 'react'

const initialState = {
  filter: {
    isNew: false,
    category: [],
  },
  status: 'idle', // idle | work | success | error
  items: [],
}
const reducer = (state, action) => {
  console.log(`Action: ${action.type}; Payload:`, action.payload)
  switch (action.type) {
    case 'filter:change': {
      return {
        ...state,
        status: 'work',
        filter: {
          ...state.filter,
          ...action.payload,
        },
      }
    }
    case 'filter:reset': {
      return {
        ...state,
        status: 'work',
        filter: {
          ...initialState.filter,
        },
      }
    }
    case 'request:start': {
      return {
        ...state,
        status: 'work',
      }
    }
    case 'request:success': {
      return {
        ...state,
        status: 'success',
        items: action.payload,
      }
    }
    case 'request:error': {
      return {
        ...state,
        status: 'error',
      }
    }
  }
}
export const useProductList = () => {
  const [state, dispatch] = useReducer(reducer, initialState)
  const updateFilter = useCallback((filter = {}) => dispatch({ type: 'filter:change', payload: filter }), [])
  const resetFilter = useCallback(() => dispatch({ type: 'filter:reset' }), [])
  const performRequest = useCallback(() => {
    dispatch({ type: 'request:start' })
    // prettier-ignore
    const serializeFilter = filter => [
      ...filter.category.map(categoryId => `category[]=${categoryId}`),
      `isNew=${filter.isNew}`,
    ].join('&')

    fetch(`/api/product?${serializeFilter(state.filter)}`)
      .then(res => {
        if (!res.ok || res.status !== 200) {
          throw new Error(`Request failed with status code ${res.status}`)
        }
        return res.json()
      })
      .then(data => dispatch({ type: 'request:success', payload: data.results }))
      .catch(err => {
        console.error(err)
        dispatch({ type: 'request:error' })
      })
  }, [state.filter])

  useEffect(() => {
    performRequest()
  }, [performRequest])

  return {
    ...state,
    updateFilter,
    resetFilter,
  }
}
