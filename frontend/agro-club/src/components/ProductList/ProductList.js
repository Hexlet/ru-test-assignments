import styles from './ProductList.module.scss'
import { useProductList } from './useProductList'

const ProductList = () => {
  const { items, filter, status, updateFilter } = useProductList()

  const handleFilterIsNewUpdate = () => updateFilter({ isNew: !filter.isNew })

  return (
    <div className={styles.root}>
      <div className={styles.filtersContainer}>
        <div>Filters placeholder</div>
        <div>
          <label htmlFor="is_new">Is new</label>
          <input id="is_new" type="checkbox" onChange={handleFilterIsNewUpdate} checked={filter.isNew} />
        </div>
      </div>
      <div>Status: {status}</div>
      <div className={styles.itemsContainer}>
        {items.map(item => (
          <div className={styles.productContainer} key={item.id}>
            <span className={styles.productName}>{item.name}</span>
            <span>{item.description}</span>
          </div>
        ))}
      </div>
    </div>
  )
}

export default ProductList
